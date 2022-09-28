#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:13:37 2022

@author: Salifu Abdullai
"""


def class_to_json(obj):
    """
    Creates a json representation of an object

    Arguments:
        obj (obj): The object inputted to create a class

    Return:
        A jason representation
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
