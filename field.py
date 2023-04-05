from typing import List

import examples
from canvas import Canvas
from point import FieldPoint, Points


class Field:
    def __init__(self, field: str = None):
        self.field_raw = field
        self.__points = self.__init_points(field)
        self.__points = self.__init_neighbours(self.points)

    def __repr__(self):
        return f"{self.__class__.__name__}(field={self.field_raw!r})"

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

    @property
    def figures(self) -> List[List[FieldPoint]]:
        figures = []  # создаём список с фигурами

        for x in range(len(self.points)):
            for y in range(len(self.points[x])):
                point = self.points[x][y]  # получаем точку из массива

                if not point.neighbours:  # если у точки нет соседей, отбрасываем её
                    continue

                if not figures:  # для первой точки
                    figures.append([point, *point.neighbours])

                else:
                    for figure in figures:
                        if point in figure:
                            figure.extend(point.neighbours)
                            break
                    else:
                        figures.append([point, *point.neighbours])

                #
                # try:
                #     next_point = self.points[x][y+1]
                #     if not next_point.neighbours:  # если у следующей точки нет соседей, отбрасываем её
                #         continue
                # except IndexError:
                #     continue
                #
                # # for figure in figures:
                # print(point, next_point)
                # # --------------------------------------------------------------------------------------------
                #
                # # сами точки и их соседи
                # intersection_result = set(point.neighbours).intersection(set(next_point.neighbours))
                #
                # if intersection_result:
                #     union_points = set(point.neighbours).union(set(next_point.neighbours))
                #     union_points.add(point)
                #     union_points.add(next_point)
                #
                # print()

                # if intersection_result:
                #     if not figures:
                #         figures.append(list(intersection_result))
                #
                #     else:
                #         for figure in figures:
                #             if point not in figure:
                #                 for figure_point in figure:
                #                     if point in figure_point.neighbours:
                #                         break
                #                 else:
                #                     figures.append(list(set(point.neighbours).union(set(next_point.neighbours))))
                #                     break
                #
                #             if next_point not in figure:
                #                 for figure_point in figure:
                #                     if next_point in figure_point.neighbours:
                #                         break
                #                 else:
                #                     figures.append(list(set(point.neighbours).union(set(next_point.neighbours))))
                #                     break
                        # else:
                        #     figures.append([point, next_point])




                # -------------------------------------------------
                #
                # if not tmp:
                #     tmp.append(point)
                #     tmp.extend(point.neighbours)
                #     tmp = list(set(tmp))
                #     result.append(tmp)
                # else:
                #     for figure in result:
                #         for neighbour in point.neighbours:
                #             if neighbour in figure:
                #                 figure.extend(point.neighbours)
                #                 figure = list(set(figure))
                #                 continue
                #             else:
                #                 tmp = []
                #                 tmp.append(neighbour)
                #                 tmp.extend(neighbour.neighbours)
                #                 tmp = list(set(tmp))
                #                 result.append(tmp)

        for i in range(len(figures)):
            figures[i] = list(set(figures[i]))

        result = []

        for figure in figures:
            if figure not in result:
                result.append(figure)

        return result



    # def __get_figure(self, point: FieldPoint):
    #     print(point)
    #     for neighbour in point.neighbours:
    #
    #     print(point.neighbours)


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
        for x in range(len(rows[0])):
            for y in range(len(rows)):
                points.append(FieldPoint(x, y, fill=rows[y][x], neighbours=None))  # TODO не None, а определение соседей

        return Points(points)

    def __init_neighbours(self, points: List[FieldPoint]) -> List[FieldPoint]:
        points = points[:]
        for row in points:
            for point in row:
                neighbours = self.__get_point_neighbour(point)
                if neighbours:
                    point.neighbours = self.__get_point_neighbour(point)

        return points

    def __get_point_neighbour(self, point: FieldPoint) -> List[FieldPoint]:
        neighbors = []

        if point.fill == "*":  # TODO Если будет не *, будет не корректно
            return []

        x = point.x
        y = point.y
        potential_neighbors = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]

        field_raw = self.field_raw.split("\n")

        for p_n in potential_neighbors:
            try:
                if field_raw[y + p_n[0]][x + p_n[1]] == ".":
                    neighbors.append(self.points[x + p_n[1]][y + p_n[0]])
            except IndexError:
                pass
        return neighbors


if __name__ == '__main__':
    field = Field(examples.hard)

    # canvas = Canvas(field.width, field.height)
    # for row in field.points:
    #     for point in row:
    #         if point.fill == ".":
    #             canvas.draw_point(point.x, point.y)

    for figure in field.figures:
        canvas = Canvas(field.width, field.height)
        print()
        for point in figure:
            if point.fill == ".":
                canvas.draw_point(point.x, point.y)
        canvas.show()
