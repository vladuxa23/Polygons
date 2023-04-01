from typing import Union, List

import examples
from canvas import CanvasPoint, Canvas


class FieldPoint(CanvasPoint):
    def __init__(
            self, x: Union[int, None] = 0, y: Union[int, None] = 0, fill: str = "*", neighbors: Union[list, None] = None
    ):
        super().__init__(x, y, fill)

        self.neighbors = neighbors

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, fill={self.fill}, neighbors={self.neighbors})"

    @property
    def neighbors(self) -> list:
        """
        Получение соседей точки

        :return: список объектов FieldPoint
        """

        return self.__neighbors

    @neighbors.setter
    def neighbors(self, value: Union[list, None]) -> None:
        """
        Установка соседей точки

        :param value: список FieldPoints
        :return: None
        """

        if not isinstance(value, (list, type(None))):
            raise TypeError(f"Expected list or None, received {type(value)}")

        if value is None:
            self.__neighbors = []
        else:
            self.__neighbors = value


class Field:
    def __init__(self, field: str = None):
        self.field_raw = field
        self.__points = self.__init_points(field)

    @property
    def width(self) -> int:
        """
        Ширина поля

        :return: значение ширины поля
        """

        result = self.field_raw.split("\n")[0]
        return len(result)

    @property
    def height(self) -> int:
        """
        Высота поля

        :return: значение высоты поля
        """

        result = self.field_raw.split("\n")
        return len(result)

    @property
    def points(self) -> List[FieldPoint]:
        """
        Список точек поля

        :return: список с FieldPoint
        """

        return self.__points

    @staticmethod
    def __init_points(field: str) -> List[FieldPoint]:
        """
        Инициализация всех точек холста

        :return: Список объектов FieldPoint
        """

        if not isinstance(field, str):
            raise TypeError(f"Expected str, received {type(field)}")

        rows = field.split("\n")
        points = []
        for y in range(len(rows[0])):
            for x in range(len(rows)):
                points.append(FieldPoint(x, y, fill=rows[x][y], neighbors=None))  # TODO не None, а определение соседей

        return points


if __name__ == '__main__':
    field = Field(examples.light)

    canvas = Canvas(field.width, field.height)
    for point in field.points:
        if point.fill == ".":
            canvas.draw_point(point.x, point.y)
    canvas.show()
