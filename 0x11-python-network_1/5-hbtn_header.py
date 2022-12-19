#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon December 19 05:14:59 2022

@author: Salifu Abdullai
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))
