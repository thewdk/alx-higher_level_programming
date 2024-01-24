#!/usr/bin/python3
"""
This is a Square class that creates a square object and initializes with size
"""


class Square:
    """
    Initialize Square object with private attribute size and check if its valid
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
