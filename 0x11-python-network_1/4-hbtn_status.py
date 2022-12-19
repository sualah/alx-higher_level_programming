#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon December 19 05:14:59 2022

@author: Salifu Abdullai
"""
from requests import get


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = get(url)
    bytes_content = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
             type(bytes_content), bytes_content)
    print(string)
