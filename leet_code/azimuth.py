import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass
from math import isclose
import math
from numbers import Real
from types import NoneType
from typing import Any, Collection, List, Optional, overload, Tuple




RELATIVE_TOLERANCE = 0.05
POS_PRECISION = 5


@dataclass(init=False)
class Point:
    latitude: float = 0.0
    longitude: float = 0.0

    @overload
    def __init__(self, arg1: Optional[Any] = None, arg2: Optional[Any] = None) -> None:
        ...

    @overload
    def __init__(self, pair: Collection[Real], _: Optional[Any]) -> None:
        ...

    @overload
    def __init__(self, coord1: Real, coord2: Real) -> None:
        ...

    def __init__(  # type:ignore[misc]
        self,
        input1: Collection[Real] | Real | None = None,
        input2: Optional[Real] = None,
    ) -> None:
        """float values with precision 6 signs after decimal dot gives accuracy 0.1m, what is redundancy, so
        we truncate signs after 6-th symbol
        """
        if isinstance(input1, Collection):
            self.latitude, self.longitude = map(lambda x: round(x, POS_PRECISION), input1)
        elif isinstance(input1, Real) and isinstance(input2, Real):
            self.latitude = round(input1, POS_PRECISION)
            self.longitude = round(input2, POS_PRECISION)
        elif not isinstance(input1, NoneType) and not isinstance(input2, NoneType):
            raise ValueError(f"Wrong type of parameters: {type(input1)},{type(input2)}")

    def __repr__(self) -> str:
        return f"[{self.latitude}, {self.longitude}]"

    def __str__(self) -> str:
        return f"[{self.latitude}, {self.longitude}]"

    def __eq__(self, b: "Point") -> bool:  # type: ignore[override]
        if isclose(self.latitude, b.latitude, rel_tol=RELATIVE_TOLERANCE) and isclose(
            self.longitude, b.longitude, rel_tol=RELATIVE_TOLERANCE
        ):
            return True
        return False

    def __ne__(self, b: "Point") -> bool:  # type: ignore[override]
        return not self.__eq__(b)



def calc_azimuth(point_a: Point, point_b: Point) -> float:
    # Convert degrees to radians
    lat1 = math.radians(point_a.latitude)
    lon1 = math.radians(point_a.longitude)
    lat2 = math.radians(point_b.latitude)
    lon2 = math.radians(point_b.longitude)

    # Calculate the difference in longitude
    delta_lon = lon2 - lon1

    # Compute the azimuth
    x = math.sin(delta_lon) * math.cos(lat2)
    y = (math.cos(lat1) * math.sin(lat2)) - (math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon))
    azimuth = math.atan2(x, y)

    # Convert azimuth from radians to degrees
    azimuth_deg = math.degrees(azimuth)

    # Normalize the azimuth to a range of 0-360 degrees
    return (azimuth_deg + 360) % 360


def approx_path_line(line: List[Point]) -> Tuple[Point, Point]:
    x_coords = [point.latitude for point in line]
    y_coords = [point.longitude for point in line]

    model = np.polyfit(x_coords, y_coords, 1)
    predict = np.poly1d(model)

    start_approx_line_x_point = x_coords[0]
    finish_approx_line_x_point = x_coords[-1]

    start_approx_line_y_point = predict(start_approx_line_x_point)
    finish_approx_line_y_point = predict(finish_approx_line_x_point)

    return (
        Point(start_approx_line_x_point, start_approx_line_y_point),
        Point(finish_approx_line_x_point, finish_approx_line_y_point),
    )





points = [
    [56.14335250854492, 37.0025520324707],
    [56.143409729003906, 37.002925872802734],
    [56.14345932006836, 37.003299713134766],
    [56.14351272583008, 37.0036735534668],
    [56.143558502197266, 37.00404739379883],
    [56.14360809326172, 37.004417419433594],

]

points = [
                [11.0, 5.0],
                [13.0, 7.5],
                [19.2, 7.5],
            ]

# points = [
#     [7.28398, 2.3899823],
#     [11.11124556, 12.32328332],
#     [32.438439, 23.9843744873],
#     [40.323829382, 45.32839283392],
# ]

precision = 5


x = [round(p[0], precision) for p in points]
y = [round(p[1], precision) for p in points]

model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
n = predict(x[0])

plt.scatter(x, y)
# r_x = range(56, 57)
# r_y = range(37, 38)

xy1 = (x[0], predict(x[0]))
xy2 = (x[-1], predict(x[-1]))
# xy2 = (56.14360809326172, np.float64(37.00440098871837))
plt.axline(xy1, xy2)
azimuth = calc_azimuth(Point(*xy1), Point(*xy2))
plt.axline(xy1, slope=azimuth)
plt.show()
pass
