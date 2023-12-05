# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:08:07 2023

@author: Tristan.Chandler
"""

def make_tags(tag, word):
    string = "<" + tag + ">" + word + "</" + tag + ">"
    return string
print(make_tags("i", "Yay"))
print(make_tags("i", "Hello"))
print(make_tags("p", "Yay"))