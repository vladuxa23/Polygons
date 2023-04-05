from typing import Union, Tuple, List


class Point:
    def __init__(self, x: Union[int, None] = 0, y: Union[int, None] = 0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point x={self.x}, y={self.y}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x!r}, y={self.y!r})"

    @property
    def x(self) -> int:
        """
        Получение значения x
        :return: значение точки x
        """

        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        """
        Установка значения точки x

        :param value: значение точки x
        :return: None
        """

        if not isinstance(value, (int, type(None))):
            raise TypeError(f"Expected int, received {type(value)}")
        self.__x = value

    @property
    def y(self) -> int:
        """
        Получение значения точки y

        :return: значение точки y
        """

        return self.__y

    @y.setter
    def y(self, value) -> None:
        """
        Установка значения точки y

        :param value: значение точки y
        :return: None
        """

        if not isinstance(value, (int, type(None))):
            raise TypeError(f"Expected int, received {type(value)}")
        self.__y = value

    @property
    def pos(self) -> Tuple[int]:
        """
        Получение значений x и y

        :return: кортеж со значениями x и y
        """

        return self.__x, self.__y


class CanvasPoint(Point):
    def __init__(self, x: Union[int, None] = 0, y: Union[int, None] = 0, fill: str = "*"):
        super(CanvasPoint, self).__init__(x, y)

        self.fill = fill

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x!r}, y={self.y!r}, fill={self.fill!r})"

    @property
    def fill(self) -> str:
        """
        Получение символа заполнения

        :return: символ заполнения
        """

        return self.__fill

    @fill.setter
    def fill(self, value: str) -> None:
        """
        Установка символа заполнения

        :param value: символ заполнения (str)
        :return: None
        """

        if not isinstance(value, str):
            raise TypeError(f"Expected str, received {type(value)}")
        self.__fill = value


class FieldPoint(CanvasPoint):
    def __init__(
            self, x: Union[int, None] = 0, y: Union[int, None] = 0, fill: str = "*", neighbours: Union[list, None] = None
    ):
        super().__init__(x, y, fill)

        self.neighbours = neighbours

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x!r}, y={self.y!r}, fill={self.fill!r})"

    @property
    def neighbours(self) -> list:
        """
        Получение соседей точки

        :return: список объектов FieldPoint
        """

        return self.__neighbours

    @neighbours.setter
    def neighbours(self, value: Union[list, None]) -> None:
        """
        Установка соседей точки

        :param value: список FieldPoints
        :return: None
        """

        if not isinstance(value, (list, type(None))):
            raise TypeError(f"Expected list or None, received {type(value)}")

        if value is None:
            self.__neighbours = []
        else:
            self.__neighbours = value


class Points:
    def __init__(self, points: List[Union[Point, FieldPoint, CanvasPoint]]) -> None:

        self.points = self.__init_points(points)

    @staticmethod
    def __init_points(points: List[Union[Point, FieldPoint, CanvasPoint]]):
        if not isinstance(points, list):
            raise TypeError(f"Expected list or None, received {type(points)}")
        # TODO Можно проверить объекты в списке

        if not points:
            return []

        result = []

        points = sorted(points, key=lambda point: point.x)

        row = []
        current_x = points[0].x

        for point in points:

            if point.x != current_x:
                result.append(row)
                row = []
                row.append(point)
                current_x = point.x
            else:
                row.append(point)
        else:
            result.append(row)  # для последнего списка

        return result

    def __getitem__(self, item):
        return self.points[item]


if __name__ == '__main__':
    points = [
        FieldPoint(x=0, y=0, fill='*', neighbors=[]), FieldPoint(x=0, y=1, fill='*', neighbors=[]),
        FieldPoint(x=0, y=2, fill='*', neighbors=[]), FieldPoint(x=0, y=3, fill='*', neighbors=[]),
        FieldPoint(x=0, y=4, fill='*', neighbors=[]), FieldPoint(x=0, y=5, fill='*', neighbors=[]),
        FieldPoint(x=0, y=6, fill='*', neighbors=[]), FieldPoint(x=0, y=7, fill='*', neighbors=[]),
        FieldPoint(x=0, y=8, fill='*', neighbors=[]), FieldPoint(x=0, y=9, fill='*', neighbors=[]),
        FieldPoint(x=1, y=0, fill='*', neighbors=[]), FieldPoint(x=1, y=1, fill='.', neighbors=[]),
        FieldPoint(x=1, y=2, fill='.', neighbors=[]), FieldPoint(x=1, y=3, fill='.', neighbors=[]),
        FieldPoint(x=1, y=4, fill='*', neighbors=[]), FieldPoint(x=1, y=5, fill='.', neighbors=[]),
        FieldPoint(x=1, y=6, fill='.', neighbors=[]), FieldPoint(x=1, y=7, fill='*', neighbors=[]),
        FieldPoint(x=1, y=8, fill='.', neighbors=[]), FieldPoint(x=1, y=9, fill='*', neighbors=[]),
        FieldPoint(x=2, y=0, fill='*', neighbors=[]), FieldPoint(x=2, y=1, fill='.', neighbors=[]),
        FieldPoint(x=2, y=2, fill='.', neighbors=[]), FieldPoint(x=2, y=3, fill='.', neighbors=[]),
        FieldPoint(x=2, y=4, fill='*', neighbors=[]), FieldPoint(x=2, y=5, fill='.', neighbors=[]),
        FieldPoint(x=2, y=6, fill='.', neighbors=[]), FieldPoint(x=2, y=7, fill='*', neighbors=[]),
        FieldPoint(x=2, y=8, fill='.', neighbors=[]), FieldPoint(x=2, y=9, fill='*', neighbors=[]),
        FieldPoint(x=3, y=0, fill='*', neighbors=[]), FieldPoint(x=3, y=1, fill='.', neighbors=[]),
        FieldPoint(x=3, y=2, fill='.', neighbors=[]), FieldPoint(x=3, y=3, fill='.', neighbors=[]),
        FieldPoint(x=3, y=4, fill='*', neighbors=[]), FieldPoint(x=3, y=5, fill='.', neighbors=[]),
        FieldPoint(x=3, y=6, fill='.', neighbors=[]), FieldPoint(x=3, y=7, fill='*', neighbors=[]),
        FieldPoint(x=3, y=8, fill='.', neighbors=[]), FieldPoint(x=3, y=9, fill='*', neighbors=[]),
        FieldPoint(x=4, y=0, fill='*', neighbors=[]), FieldPoint(x=4, y=1, fill='.', neighbors=[]),
        FieldPoint(x=4, y=2, fill='.', neighbors=[]), FieldPoint(x=4, y=3, fill='.', neighbors=[]),
        FieldPoint(x=4, y=4, fill='*', neighbors=[]), FieldPoint(x=4, y=5, fill='.', neighbors=[]),
        FieldPoint(x=4, y=6, fill='.', neighbors=[]), FieldPoint(x=4, y=7, fill='*', neighbors=[]),
        FieldPoint(x=4, y=8, fill='.', neighbors=[]), FieldPoint(x=4, y=9, fill='*', neighbors=[]),
        FieldPoint(x=5, y=0, fill='*', neighbors=[]), FieldPoint(x=5, y=1, fill='.', neighbors=[]),
        FieldPoint(x=5, y=2, fill='.', neighbors=[]), FieldPoint(x=5, y=3, fill='.', neighbors=[]),
        FieldPoint(x=5, y=4, fill='*', neighbors=[]), FieldPoint(x=5, y=5, fill='.', neighbors=[]),
        FieldPoint(x=5, y=6, fill='.', neighbors=[]), FieldPoint(x=5, y=7, fill='*', neighbors=[]),
        FieldPoint(x=5, y=8, fill='.', neighbors=[]), FieldPoint(x=5, y=9, fill='*', neighbors=[]),
        FieldPoint(x=6, y=0, fill='*', neighbors=[]), FieldPoint(x=6, y=1, fill='.', neighbors=[]),
        FieldPoint(x=6, y=2, fill='.', neighbors=[]), FieldPoint(x=6, y=3, fill='.', neighbors=[]),
        FieldPoint(x=6, y=4, fill='*', neighbors=[]), FieldPoint(x=6, y=5, fill='.', neighbors=[]),
        FieldPoint(x=6, y=6, fill='.', neighbors=[]), FieldPoint(x=6, y=7, fill='*', neighbors=[]),
        FieldPoint(x=6, y=8, fill='.', neighbors=[]), FieldPoint(x=6, y=9, fill='*', neighbors=[]),
        FieldPoint(x=7, y=0, fill='*', neighbors=[]), FieldPoint(x=7, y=1, fill='*', neighbors=[]),
        FieldPoint(x=7, y=2, fill='*', neighbors=[]), FieldPoint(x=7, y=3, fill='*', neighbors=[]),
        FieldPoint(x=7, y=4, fill='*', neighbors=[]), FieldPoint(x=7, y=5, fill='*', neighbors=[]),
        FieldPoint(x=7, y=6, fill='*', neighbors=[]), FieldPoint(x=7, y=7, fill='*', neighbors=[]),
        FieldPoint(x=7, y=8, fill='*', neighbors=[]), FieldPoint(x=7, y=9, fill='*', neighbors=[]),
        FieldPoint(x=8, y=0, fill='*', neighbors=[]), FieldPoint(x=8, y=1, fill='.', neighbors=[]),
        FieldPoint(x=8, y=2, fill='.', neighbors=[]), FieldPoint(x=8, y=3, fill='.', neighbors=[]),
        FieldPoint(x=8, y=4, fill='*', neighbors=[]), FieldPoint(x=8, y=5, fill='.', neighbors=[]),
        FieldPoint(x=8, y=6, fill='.', neighbors=[]), FieldPoint(x=8, y=7, fill='*', neighbors=[]),
        FieldPoint(x=8, y=8, fill='.', neighbors=[]), FieldPoint(x=8, y=9, fill='*', neighbors=[])
    ]

    points = Points(points)
    print(points[3][3])
