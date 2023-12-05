# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:21:21 2023

@author: Tristan.Chandler
"""


number = int(input("Enter a number: "))

n = number
summation = 0

for i in range(1, n+1):
    summation += i

print(n,"summation is: ", end="")
print(summation)