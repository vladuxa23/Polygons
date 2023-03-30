from typing import Union, List

from examples import light
from point import Point


class Polygon:
    def __init__(self, angle_points: Union[list, None] = None):
        self.angle_points = [] if angle_points is None else angle_points

    def __str__(self) -> str:
        return f"Polygon with points = {self.angle_points}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(angle_points={self.angle_points})"

    @property
    def angle_points(self) -> List[Point]:
        return self.__angle_points

    @angle_points.setter
    def angle_points(self, value) -> None:
        if not isinstance(value, list):
            raise TypeError(f"Expected list, received {type(value)}")

        self.__angle_points = value

    def append_point(self, point: Point) -> None:
        if not isinstance(point, Point):
            raise TypeError(f"Expected Point, received {type(point)}")

        self.__angle_points.append(point)

    @property
    def max_x(self) -> Point:
        return max(self.angle_points, key=lambda point: point.x)

    @property
    def max_y(self) -> Point:
        return max(self.angle_points, key=lambda point: point.y)

    def show(self):
        print(self.max_x)
        print(self.max_y)
