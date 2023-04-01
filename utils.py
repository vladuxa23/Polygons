from typing import List

from examples import light
from point import Point
from polygon import Polygon


class PolygonDetector:

    @staticmethod
    def is_polygon_next_x_point(polygon: Polygon, point: Point):

        if not isinstance(polygon, Polygon):
            raise TypeError(f"Expected Polygon, received {type(point)}")

        if not isinstance(point, Point):
            raise TypeError(f"Expected Point, received {type(point)}")

        for polygon_point in polygon.points:
            if polygon_point.x + 1 == point.x:
                # print(polygon_point.x + 1, point.x)
                return True
        return False

    @staticmethod
    def detect(polygons_field: List[str], polygon_char: str = "."):
        """

        :param polygon:
        :return:
        """

        polygons = []

        rows = polygons_field.split("\n")

        print(polygons_field)

        for y, row in enumerate(rows):
            for x, char in enumerate(row):
                # print(x, y, char)
                if char == polygon_char:
                    if not polygons:
                        new_polygon = Polygon()
                        new_polygon.append_point(Point(x, y))
                        polygons.append(new_polygon)
                    else:
                        for polygon in polygons:
                            if PolygonDetector.is_polygon_next_x_point(polygon, Point(x, y)):
                                polygon.append_point(Point(x, y))
                        else:
                            new_polygon = Polygon()
                            new_polygon.append_point(Point(x, y))
                            polygons.append(new_polygon)

        for polygon in polygons:
            print(polygon.show())


PolygonDetector.detect(light)
