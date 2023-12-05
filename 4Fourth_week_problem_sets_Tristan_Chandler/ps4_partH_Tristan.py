# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:01:04 2023

@author: Tristan.Chandler
"""

def combo_string(word1,word2):
    if len(word1) >= 5:
        return word2 + word1 + word2
    elif len(word1) == 3:
        return word2 + word1 + word2
    else:
        return word1 + word2 + word1
print(combo_string("Hello", "hi"))
print(combo_string("hi", "Hello"))
print(combo_string("aaa", "b"))    