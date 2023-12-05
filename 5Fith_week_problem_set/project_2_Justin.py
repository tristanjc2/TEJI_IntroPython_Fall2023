#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 00:06:42 2023

@author: justin
"""

print("Think of a number between 1 and 100.")

lower_bound = 1
upper_bound = 1001

guess = 500
answer = input("Is the number " + str(guess) + "? (yes, higher, lower) ")

while answer != "yes":
    if answer == "higher":
        lower_bound = guess
    elif answer == "lower":
        upper_bound = guess
    guess = (lower_bound + upper_bound) // 2
    answer = input("Is the number " + str(guess) + "? (yes, higher, lower) ")

    