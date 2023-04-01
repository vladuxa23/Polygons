from typing import List

from canvas import Canvas
from point import Point


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
        self.points = self.__init_points(self.start, self.end)

    def __str__(self) -> str:
        return f"Line {self.points}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(start={self.start}, end={self.end})"

    @property
    def start(self) -> Point:
        """
        Получение начальной точки линии

        :return: начальная точка Point
        """

        return self.__start

    @start.setter
    def start(self, value: Point) -> None:
        """
        Установка начальной точки линии

        :param value: начальная точка Point
        :return: None
        """

        if not isinstance(value, Point):
            raise TypeError(f"Expected Point, received {type(value)}")

        self.__start = value

    @property
    def end(self) -> Point:
        """
        Получение конечной точки линии

        :return: конечная точка Point
        """

        return self.__end

    @end.setter
    def end(self, value: Point) -> None:
        """
        Установка начальной точки линии

        :param value: конечная точка Point
        :return: None
        """

        if not isinstance(value, Point):
            raise TypeError(f"Expected Point, received {type(value)}")

        self.__end = value

    @property
    def max_x(self) -> Point:
        """
        Получение максимальной точки по координате x

        :return: максимальная точка по координате x
        """

        return max(self.points, key=lambda point: point.x)

    @property
    def max_y(self) -> Point:
        """
        Получение максимальной точки по координате y

        :return: максимальная точка по координате y
        """

        return max(self.points, key=lambda point: point.y)

    @property
    def min_x(self) -> Point:
        """
        Получение минимальной точки по координате x

        :return: минимальная точка по координате x
        """

        return min(self.points, key=lambda point: point.x)

    @property
    def min_y(self) -> Point:
        """
        Получение минимальной точки по координате y

        :return: минимальная точка по координате y
        """

        return min(self.points, key=lambda point: point.y)

    @staticmethod
    def __init_points(start: Point, end: Point) -> List[Point]:
        """
        Инициализация точек, которые занимает линия

        :param start: начальная точка
        :param end: конечная точка
        :return: список с объектами Point
        """

        if not isinstance(start, Point):
            raise TypeError(f"Expected Point, received {type(start)}")

        if not isinstance(end, Point):
            raise TypeError(f"Expected Point, received {type(end)}")

        x1, y1, x2, y2 = end.y, end.x, start.y, start.x
        points = []
        rev = False

        is_steep = abs(y2 - y1) > abs(x2 - x1)

        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            rev = True

        delta_x = x2 - x1
        delta_y = abs(y2 - y1)
        error = int(delta_x / 2)
        y = y1

        if y1 < y2:
            y_step = 1
        else:
            y_step = -1

        for x in range(x1, x2 + 1):
            if is_steep:
                points.append(Point(y, x))
            else:
                points.append(Point(x, y))
            error -= delta_y
            if error < 0:
                y += y_step
                error += delta_x

        # Переворачиваем список, если координаты были перевернуты
        if rev:
            points.reverse()
        return points

    def show(self, canvas: Canvas) -> None:
        """
        Отрисовка фигуры на холсте

        :param canvas: объект Canvas
        :return: None
        """

        for point in self.points:
            canvas.draw_point(point.x, point.y)
        canvas.show()


if __name__ == '__main__':
    line = Line(Point(1, 1), Point(10, 17))
    canvas = Canvas(20, 20)
    line.show(canvas)
