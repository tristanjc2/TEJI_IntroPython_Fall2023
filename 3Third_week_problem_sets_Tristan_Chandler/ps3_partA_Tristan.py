# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:14:29 2023

@author: Tristan.Chandler
"""

credits = eval(input("Enter the number of credits: "))

if credits <= 23:
    print("You are a freshman.")
elif credits <= 53 and credits >= 24:
    print("You are a sophomore.")
elif credits <= 83 and credits >= 54:
    print("You are a junior.")
else:
    print("You are a senior.")