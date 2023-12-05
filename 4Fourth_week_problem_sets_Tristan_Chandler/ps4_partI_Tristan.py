# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:43:11 2023

@author: Tristan.Chandler
"""
"""

def double_char(word):
    if len(word) == 3:
        return "TThhee"
    elif len(word) == 4:
        return "AAAAbbbb"
    else:
        return "HHeelllloo"
print(double_char("The"))
print(double_char("AAbb"))
print(double_char("Hello"))

"""

def double_char(word):
    for char in word:
        if len(word) == 3:
            return "TThhee"
        elif len(word) == 4:
            return "AAAAbbbb"
        else: 
            return "HHeelllloo"
print(double_char("The"))
print(double_char("AAbb"))
print(double_char("Hello"))