#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:13:37 2022

@author: Salifu Abdullai
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class shape, inheirts from Rectangle and BaseGeometry
    """
    def __init__(self, size):
        """"
        Init function for Square

        Attributes:
            size (int): The size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size


    def __str__(self):
        """
        str funtion for rectangle

        Returns:
            Return width/height
        """
        return '[Rectangle] ' + str(self.__size) + '/' + str(self.__size)


    def area(self):
        """
        Calculates the area of the rectangle

        Return:
           The area of the rectangle
        """
        return self.__size * self.__size
