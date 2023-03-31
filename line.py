from canvas import Canvas
from point import Point


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
        self.points = self.__init_points()

    def __str__(self) -> str:
        return f"Line {self.points}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(start={self.start}, end={self.end})"

    @property
    def start(self) -> Point:
        return self.__start

    @start.setter
    def start(self, value: Point) -> None:
        if not isinstance(value, Point):
            raise TypeError(f"Expected Point, received {type(value)}")

        self.__start = value

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError(f"Expected Point, received {type(value)}")

        self.__end = value

    @property
    def max_x(self) -> Point:
        return max(self.points, key=lambda point: point.x)

    @property
    def max_y(self) -> Point:
        return max(self.points, key=lambda point: point.y)

    @property
    def min_x(self) -> Point:
        return min(self.points, key=lambda point: point.x)

    @property
    def min_y(self) -> Point:
        return min(self.points, key=lambda point: point.y)

    def __init_points(self) -> None:
        x1, y1, x2, y2 = self.start.x, self.start.y, self.end.x, self.end.y

        points = []
        issteep = abs(y2 - y1) > abs(x2 - x1)
        if issteep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        rev = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            rev = True
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x1, x2 + 1):
            if issteep:
                points.append(Point(y, x))
            else:
                points.append(Point(x, y))
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
        # Reverse the list if the coordinates were reversed
        if rev:
            points.reverse()
        return points

    def show(self) -> None:
        canvas = Canvas(20, 20)
        for point in self.points:
            canvas.draw_point(point.x, point.y)
        canvas.show()


if __name__ == '__main__':
    line = Line(Point(1, 1), Point(7, 3))
    line.show()
