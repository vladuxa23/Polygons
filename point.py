from typing import Union


class Point:
    def __init__(self, x: Union[int, None] = 0, y: Union[int, None] = 0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point x={self.x}, y={self.y}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        if not isinstance(value, (int, type(None))):
            raise TypeError(f"Expected int, received {type(value)}")
        self.__x = value

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, value) -> None:
        if not isinstance(value, (int, type(None))):
            raise TypeError(f"Expected int, received {type(value)}")
        self.__y = value
