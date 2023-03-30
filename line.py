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
        # if self.start.x < self.end.x:
        #     self.start.x = -1 * self.start.x
        #     self.end.x = -1 * self.end.x
        points = []
        for x in range(self.start.x, self.end.x+1):
            for y in range(self.start.y, self.end.y+1):
                points.append(Point(x, y))

        return points

    def show(self) -> None:
        # По логике надо писать класс для отображения конкретной фигуры, которую ему передаём
        result = ""
        for x in range(self.max_x.x + 2):
            for y in range(self.max_y.y + 2):
                if Point(x, y) in self.points:
                    result += "."
                else:
                    result += "*"
            result += "\n"

        print(result)

if __name__ == '__main__':
    line = Line(Point(1,1), Point(2, 3))
    # print(line.points)
    line.show()