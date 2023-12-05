# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:51:49 2023

@author: Tristan.Chandler
"""

def has_underscores(word):
    for char in word:
        if "_" in word:
            return True
        else:
            return False
print(has_underscores("b _ a r s!"))
print(has_underscores("b e a r s!"))
print(has_underscores("b_ _ _ _!"))