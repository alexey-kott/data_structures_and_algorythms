import asyncio
import logging
from concurrent.futures import ProcessPoolExecutor
from typing import Collection, Callable

WORKER_LIMIT = 8

logger = logging.getLogger(__name__)


def generate_thumbnail(data: bytes) -> bytes:
    """Resize image to fit a thumbnail size"""
    ...


class Connect:
    """This is an interface; you can't change it."""

    def is_read_ready(self) -> bool:
        """Checks if connect is ready to read"""
        ...

    def is_write_ready(self) -> bool:
        """Checks if connect is ready to write"""
        ...

    def read(self) -> bytes:
        """Waits until ready then reads data"""
        ...


    def write(self, data: bytes):
        """Waits until ready then writes data"""
        ...


async def async_wrapper(executor: ProcessPoolExecutor, func: Callable, *args, **kwargs):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, func, *args)
    return result


def process_image(connect: Connect) -> None:
    while True:
        if connect.is_read_ready():
            image = connect.read()
            break
    logger.info(f'received {len(image)} bytes successfully')
    thumbnail = generate_thumbnail(image)
    logger.info('thumbnail generate successfully')
    while True:
        if connect.is_write_ready():
            connect.write(thumbnail)
            break
    logger.info('process finished')



async def async_process(connects: Collection[Connect]):
    tasks = []
    with ProcessPoolExecutor(max_workers=WORKER_LIMIT) as executor:
        for connect in connects:
            tasks.append(async_wrapper(executor, process_image, connect))

    result = await asyncio.gather(*tasks, return_exceptions=True)

    for item in result:
        if isinstance(item, Exception):
            logger.error('something went wrong: %s', item)
        else:
            logger.info('processing successes')



def process(connects: list[Connect]):
    asyncio.run(async_process(connects))

    # ----------
    # for connect in connects:
    #     image = connect.read()
    #     thumbnail = generate_thumbnail(image)
    #     connect.write(thumbnail)



async def get_weather(

):
    gismeteo_client = GismeteoClient()
    gismeteo_weather = await gismeteo_client.get_weather()

    yandex_client = YandexClient()
    yandex_weather = await yandex_client.get_weather()

    return {"yandex_weather": yandex_weather, "gismeteo_weather": gismeteo_weather}