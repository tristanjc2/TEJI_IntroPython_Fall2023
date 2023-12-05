# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:56:52 2023

@author: Tristan.Chandler
"""

number = int(input("Enter a number to find the factorial: "))

n = number
factor = 1
 
for i in range(1, n+1):
    factor = factor * i
 
print("The factorial of",n,"is: ", end="")
print(factor)