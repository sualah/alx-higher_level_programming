#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon December 19 05:14:59 2022

@author: Salifu Abdullai
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    response = post(url, data=email)
    print(response.text)
