#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:13:37 2022

@author: Salifu Abdullai
"""


def read_file(filename=""):
    """
    Reads the file

    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
