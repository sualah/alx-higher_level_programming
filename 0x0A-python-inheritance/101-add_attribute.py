#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:13:37 2022

@author: Salifu Abdullai
"""


def add_attribute(obj, name, value):
    """
    Add attribute into the class if it's possible

    Arguments:
        obj (object): The object to set as attribute
        name (str): Name for the new attribute
        value (int): Value to new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
