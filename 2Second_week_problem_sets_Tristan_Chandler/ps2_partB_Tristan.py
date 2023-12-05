# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:23:18 2023

@author: Tristan.Chandler
"""

name = str(input("Please enter your name: "))
vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
constanants = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w', 'y', 'B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'V', 'X', 'Z', 'H', 'R', 'W', 'Y']

name = name.lower()

#Added .lower() to minimize/clean up code below and obove in the list. Left it in for reference.

count = 0
i = 0

for i in range(len(name)):
    if (
        (name[i] == "a")
        or (name[i] == "e")
        or (name[i] == "i")
        or (name[i] == "o")
        or (name[i] == "u")
    ):
        count += 1

count2 = 0
i2 = 0

for i2 in range(len(name)):
    if (
        (name[i2] == "b")
        or (name[i2] == "c")
        or (name[i2] == "d")
        or (name[i2] == "f")
        or (name[i2] == "g")
        or (name[i2] == "j")
        or (name[i2] == "k")
        or (name[i2] == "l")
        or (name[i2] == "m")
        or (name[i2] == "n")
        or (name[i2] == "p")
        or (name[i2] == "q")
        or (name[i2] == "s")
        or (name[i2] == "t")
        or (name[i2] == "v")
        or (name[i2] == "x")
        or (name[i2] == "z")
        or (name[i2] == "h")
        or (name[i2] == "r")
        or (name[i2] == "w")
        or (name[i2] == "y")
    ):
        count2 += 1
        
print("You have",count, "vowels in your name.")
print("You have",count2, "constonants in your name.")