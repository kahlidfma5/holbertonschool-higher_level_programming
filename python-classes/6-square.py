#!/usr/bin/python3
""" Module Square """


class Square:
    """ Define a square by size """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.size):
                print(" " * self.__position[0], end="")
                print("#" * self.size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        msg = 'position must be a tuple of 2 positive integers'
        if len(value) != 2 or type(value) != tuple:
            raise TypeError(msg)
        if type(value[0]) != int or value[0] < 0:
            raise TypeError(msg)
        if type(value[1]) != int or value[1] < 0:
            raise TypeError(msg)
        self.__position = value
