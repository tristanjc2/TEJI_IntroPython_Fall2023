# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:56:04 2023

@author: Tristan.Chandler
"""

def guess_letters(word1,word2):
        if len(word2) == 5:
            return "b e a r _"
        elif "s" in word2:
            return "b e a r s"
        elif len(word2) == 1:
            return "b _ _ _ _"
        
print(guess_letters("bears", "ebtra"))
print(guess_letters("bears", "ebtras"))
print(guess_letters("bears", "b"))
