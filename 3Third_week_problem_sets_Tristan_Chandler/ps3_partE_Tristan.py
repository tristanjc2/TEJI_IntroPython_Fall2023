# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:35:51 2023

@author: Tristan.Chandler
"""

columns = int(input("How high should the triangle be?: "))


for i in range(columns):
    print("* " * (columns-i))
