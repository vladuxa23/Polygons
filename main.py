from typing import List

import examples
from canvas import Canvas
from field import Field
from point import FieldPoint


def draw_figures(figures, field_width=40, field_height=20):
    for figure in figures:
        canvas = Canvas(field_width, field_height)
        for point in figure:
            if point.fill == ".":
                canvas.draw_point(point.x, point.y)
        canvas.show()
        print()


def draw_figure(figure: List[FieldPoint], field_width=40, field_height=20):
    canvas = Canvas(field_width, field_height)

    for point in figure:
        if point.fill == ".":
            canvas.draw_point(point.x, point.y)
    canvas.show()
    print()


field = Field(examples.light)
# draw_figures(field.figures, field.width, field.height)  # Раскомментировать, чтобы распечатать обнаруженные фигуры
print(f"Самая большая фигура площадью {len(field.max_figure)} точек")
draw_figure(field.max_figure)

field = Field(examples.medium)
# draw_figures(field.figures, field.width, field.height)  # Раскомментировать, чтобы распечатать обнаруженные фигуры
print(f"Самая большая фигура площадью {len(field.max_figure)} точек")
draw_figure(field.max_figure)

field = Field(examples.medium_2)
# draw_figures(field.figures, field.width, field.height)  # Раскомментировать, чтобы распечатать обнаруженные фигуры
print(f"Самая большая фигура площадью {len(field.max_figure)} точек")
draw_figure(field.max_figure)

field = Field(examples.hard)
# draw_figures(field.figures, field.width, field.height)  # Раскомментировать, чтобы распечатать обнаруженные фигуры
print(f"Самая большая фигура площадью {len(field.max_figure)} точек")
draw_figure(field.max_figure)

field = Field(examples.hard_2)
# draw_figures(field.figures, field.width, field.height)  # Раскомментировать, чтобы распечатать обнаруженные фигуры
print(f"Самая большая фигура площадью {len(field.max_figure)} точек")
draw_figure(field.max_figure)

field = Field(examples.hard_3)
# draw_figures(field.figures, field.width, field.height)  # Раскомментировать, чтобы распечатать обнаруженные фигуры
print(f"Самая большая фигура площадью {len(field.max_figure)} точек")
draw_figure(field.max_figure)

