# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:14:01 2023

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


def count_vowels(word):
    count = 0
    for char in word:
        if is_vowel(char):
            count += 1
    return count
print(count_vowels("justin"))
print(count_vowels("bcdfgh"))
print(count_vowels("yo"))
