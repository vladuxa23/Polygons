import examples
from canvas import Canvas
from field import Field

field = Field(examples.hard_2)

# Раскомментировать, чтобы распечатать обнаруженные фигуры
# for figure in field.figures:
#     canvas = Canvas(field.width, field.height)
#     for point in figure:
#         if point.fill == ".":
#             canvas.draw_point(point.x, point.y)
#     canvas.show()
#     print()


print(f"Самая большая фигура площадью {len(field.max_figure)} точек")

