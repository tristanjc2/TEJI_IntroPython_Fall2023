# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:20:05 2023

@author: Tristan.Chandler
"""

# BOTH CODE BLOCKS WORK

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))

highestnum = [num1, num2, num3, num4, num5]
highestnum.sort()

for i in range(1):
    print("The maximum number was:", max(highestnum))






"""
nums = [int(input("Enter a number: ")) for i in range(5)]
print("The maximum number was:", max(nums))
"""

