# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:11:54 2023

@author: Tristan.Chandler
"""

def is_vowel(letter):
    vowels = ['a','e','i','o','u']
    if letter in vowels:
        return True
    else:
        return False
print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel("c"))