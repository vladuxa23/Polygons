from typing import Union, Tuple


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
        """
        Получение значения x
        :return: значение точки x
        """

        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        """
        Установка значения точки x

        :param value: значение точки x
        :return: None
        """

        if not isinstance(value, (int, type(None))):
            raise TypeError(f"Expected int, received {type(value)}")
        self.__x = value

    @property
    def y(self) -> int:
        """
        Получение значения точки y

        :return: значение точки y
        """

        return self.__y

    @y.setter
    def y(self, value) -> None:
        """
        Установка значения точки y

        :param value: значение точки y
        :return: None
        """

        if not isinstance(value, (int, type(None))):
            raise TypeError(f"Expected int, received {type(value)}")
        self.__y = value

    @property
    def pos(self) -> Tuple[int]:
        """
        Получение значений x и y

        :return: кортеж со значениями x и y
        """

        return self.__x, self.__y
