"""
Есть пользовательская обученная модель, которую обучили с помощью automl задачи обучения.
job_id - ID задачи обучения

Внутри обученная модель умеет делать предсказания
    model.predict([0.1, 0.2, 0.1]) = 1

От бизнеса пришла задача:
Хочу, чтобы была ручка
@app.route("/automl/<job_id>/batch/predict", methods=["POST"])
def send_batch_predict...
Которая на вход принимает путь до файла на S3 хранилище, с запросами на предсказания
 [
    [0.1, 0.2, 0.1],
    [0.3, 0.2, 0.1],
    [0.2, 0.4, 0.1]
 ]
делает предсказания и результат складывает в S3 хранилище

Нужно разобраться в коде. Найти ошибки. Код разбить по отдельным модулям.
Возможно, предложить другое архитектурное решение.
"""
import re
import time
import logging
from typing import Dict, List, Tuple, Optional, Union
from json import JSONDecodeError
from simplejson.errors import JSONDecodeError as SimpleJSONDecodeError
import requests
import boto3
import botocore.exceptions
from functools import wraps
from asgi import limiter
from flask import Blueprint, jsonify, request, Response
from utils import (
    check_api_key,
    get_ns_from_headers,
)
from config import (
    INFERENCE_PREDICT_IP,
    BATCH_PREDICT_AUTOML_IMAGE,
    BATCH_PREDICT_REQUEST_TIMEOUT,
    INFERENCE_GWAPI_ADDR,
)

app = Blueprint("batch_predict", __name__)
logger = logging.getLogger(__name__)


def validate_job_id(func):
    re_uuid = re.compile(r"\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b")

    @wraps(func)
    def wrapper(*args, job_id: str, **kwargs):
        if job_id and re_uuid.match(job_id.lower()):
            return func(*args, job_id=job_id, **kwargs)
        return jsonify({"status": "error", "message": "Invalid job_id"}), 400

    return wrapper


def get_batch_services(job_id: str) -> Tuple[Optional[List[Dict]], Optional[Tuple[Dict, int]]]:
    url = f"http://{INFERENCE_GWAPI_ADDR}/api/service/v1"
    headers = {"X-Namespace": get_ns_from_headers(request.headers)}
    params = {"automl_job_id": job_id}

    with requests.get(url, params=params, headers=headers) as resp:
        try:
            inference_service_info = resp.json()
        except (JSONDecodeError, SimpleJSONDecodeError) as e:
            inference_service_info = resp.text
        return inference_service_info, None


def validate_predict_request(req):
    payload_required_fields = [
        "s3_endpoint_url",
        "aws_access_key_id",
        "aws_secret_access_key",
        "bucket",
        "batch_key",
        "result_dir_key",
    ]
    payload = getattr(req, "json", {})
    if (
        not isinstance(payload, dict)
        or not isinstance(payload.get("instances"), list)
        or len(payload["instances"]) != 1
        or not isinstance(payload["instances"][0], dict)
    ):
        return "Invalid instances list"

    if missing_fields := [f for f in payload_required_fields if f not in payload["instances"][0]]:
        return f"Missing fields in prediction request: {','.join(missing_fields)}"

    client_s3 = boto3.client(
        service_name="s3",
        endpoint_url=payload["instances"][0]["s3_endpoint_url"],
        aws_access_key_id=payload["instances"][0]["aws_access_key_id"],
        aws_secret_access_key=payload["instances"][0]["aws_secret_access_key"],
    )
    try:
        client_s3.head_bucket(Bucket=payload["instances"][0]["bucket"])
    except (botocore.exceptions.ClientError, botocore.exceptions.EndpointConnectionError, ValueError):
        return f"S3 bucket {payload['instances'][0]['bucket']} is inaccessible"


@app.route("/automl/<job_id>/batch/predict", methods=["POST"])
@limiter.limit("30/minute;1000/day")
@check_api_key
@validate_job_id
def send_batch_predict(job_id: str):
    if validation_error := validate_predict_request(request):
        return (
            jsonify({"status": "error", "details": validation_error}),
            400,
        )

    services, _err = get_batch_services(job_id)
    if _err:
        return _err

    # Check if batch predict inference service is not running
    if not services:
        _result = create_batch_predict_service(job_id=job_id)
        return _result, 200
    elif len(services) > 1:
        logger.error(f"Found multiple inference services with automl_job_id={job_id}")
        return jsonify({"status": "error", "details": f"Invalid service configuration for {job_id=}"}), 500

    # Check for inference service pod status
    if not services[0]["isReady"]:
        return (
            jsonify(
                {"status": "error", "details": f"Batch prediction inference service with {job_id=} not ready"}
            ),
            409,
        )

    # Using negligible read timeout to close connection instantly
    try:
        timeout = (None, float(BATCH_PREDICT_REQUEST_TIMEOUT))
    except ValueError:
        logger.warning("Unable to cast BATCH_PREDICT_REQUEST_TIMEOUT to float")
        pass

    job_name = services[0]["metadata"]["name"]
    namespace = get_ns_from_headers(request.headers)
    try:
        return simple_request(
            f"http://{INFERENCE_PREDICT_IP}/v1/models/{job_name}:predict",
            "POST",
            headers={
                "Host": f"{job_name}.{namespace}.example.com",
            },
            timeout=timeout,
        )
    except requests.exceptions.ReadTimeout:
        # ReadTimeout is raised intentionally due to low read timeout
        pass

    return jsonify({"status": "success", "details": f"Sent batch prediction request for {job_id=}"})


def create_batch_predict_service(job_id: str):
    services, _err = get_batch_services(job_id)
    if _err:
        return _err
    # Check if batch predict inference service is not running
    if len(services) != 0:
        return (
            jsonify(
                {"status": "error", "details": f"Batch prediction inference service with {job_id=} already exists"}
            ),
            400,
        )
    result = make_request(
        method="POST",
        url=f"http://{INFERENCE_GWAPI_ADDR}/api/service/v1/",
        headers={
            **request.headers,
            "X-Namespace": get_ns_from_headers(request.headers),
        },
        json={
            "name": f"batchpredict-{int(time.time())}",
            "image": BATCH_PREDICT_AUTOML_IMAGE,
            "app_name": "batchpredictservice",
        },
    )

    return result


def make_request(method, url, headers=None, data=None, json=None, **kwargs):
    with requests.request(method, url, headers=headers, data=data, json=json, **kwargs) as resp:
        if not resp.ok:
            logger.error(f"{method} {url} failed with code {resp.status_code}:")
            logger.error(resp.text)
        try:
            return jsonify(resp.json()), resp.status_code
        except (JSONDecodeError, SimpleJSONDecodeError):
            return jsonify({"status": "success" if resp.ok else "error", "message": resp.text}), resp.status_code


def simple_request(
    url: str, method: str, headers=None, json=None, stream=False, **kwargs
) -> Tuple[Union[Response, str], int]:
    if json is None and request.data:
        json = request.json

    try:
        response = requests.request(
            method=method,
            url=url,
            params=request.args,
            json=json,
            headers=headers,
            stream=stream,
            **kwargs,
        )
    except Exception as e:
        raise

    try:
        return jsonify(response.json()), response.status_code
    except (json.decoder.JSONDecodeError, ValueError):
        return response.text, response.status_code
