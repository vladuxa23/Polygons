from typing import List

from point import CanvasPoint


class Canvas:
    def __init__(self, width: int, height: int, fill: str = "*"):
        self.width = width
        self.height = height
        self.background_fill = fill
        self.points = self.__init_points()

    def __repr__(self):
        return f"{self.__class__.__name__}(width={self.width!r}, height={self.height!r}, fill={self.background_fill!r})"

    @property
    def width(self) -> int:
        """
        Получение ширины холста

        :return: значение ширины холста
        """

        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        Установка ширины холста

        :return: None
        """

        if not isinstance(value, int):
            raise TypeError(f"Expected int, received {type(value)}")

        self.__width = value

    @property
    def height(self) -> int:
        """
        Получение высоты холста

        :return: высота холста
        """

        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        Установка высоты холста

        :param value: значение высоты холста
        :return: None
        """

        if not isinstance(value, int):
            raise TypeError(f"Expected int, received {type(value)}")

        self.__height = value

    # @property
    # def fill_points(self) -> list:
    #     """
    #
    #     :return:
    #     """
    #
    #     return self.__fill_points
    #
    # @fill_points.setter
    # def fill_points(self, value) -> None:
    #     if not isinstance(value, list):
    #         raise TypeError(f"Expected list, received {type(value)}")
    #     self.__fill_points = value

    def draw_point(self, x: int, y: int) -> None:
        """
        Отрисовка точки на холсте

        :param x: значение точки x
        :param y: значение точки y
        :return: None
        """

        if not isinstance(x, int):
            raise TypeError(f"Expected int, received {type(x)}")

        if not isinstance(y, int):
            raise TypeError(f"Expected int, received {type(y)}")

        for point in self.points:
            if point.x == x and point.y == y:
                point.fill = "."

    def show(self) -> None:
        """
        Отрисовка холста в консоли

        :return: None
        """

        field = [["" for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.width):
            for y in range(self.height):
                for point in self.points:
                    if point.x == x and point.y == y:
                        field[y][x] = point.fill
                        break

        for row in field:
            print("".join(row))

    def __init_points(self) -> List[CanvasPoint]:
        """
        Инициализация всех точек холста

        :return: Список объектов CanvasPoint
        """

        points = []
        for x in range(self.width):
            for y in range(self.height):
                points.append(CanvasPoint(x, y))

        return points


if __name__ == '__main__':
    canvas = Canvas(10, 15)

    canvas.draw_point(1, 2)
    canvas.draw_point(1, 3)
    canvas.draw_point(1, 4)
    canvas.draw_point(1, 5)
    canvas.draw_point(1, 6)

    canvas.show()
