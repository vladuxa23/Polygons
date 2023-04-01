from typing import Union, List

from point import Point


class Polygon:
    def __init__(self, points: Union[list, None] = None):
        self.points = [] if points is None else points

    def __str__(self) -> str:
        return f"Polygon with points = {self.points}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(angle_points={self.points})"

    @property
    def points(self) -> List[Point]:
        return self.__points

    @points.setter
    def points(self, value) -> None:
        if not isinstance(value, list):
            raise TypeError(f"Expected list, received {type(value)}")

        self.__points = value

    def append_point(self, point: Point) -> None:
        if not isinstance(point, Point):
            raise TypeError(f"Expected Point, received {type(point)}")

        self.__points.append(point)

    @property
    def max_x(self) -> Point:
        return max(self.points, key=lambda point: point.x)

    @property
    def max_y(self) -> Point:
        return max(self.points, key=lambda point: point.y)

    def show(self):
        print(self.max_x)
        print(self.max_y)
