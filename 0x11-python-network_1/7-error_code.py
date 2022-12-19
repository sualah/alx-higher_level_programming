#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon December 19 05:14:59 2022

@author: Salifu Abdullai
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    response = get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print('Error code: {}'.format(response.status_code))
