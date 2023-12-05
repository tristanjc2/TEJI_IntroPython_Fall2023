# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:00:52 2023

@author: Tristan.Chandler
"""

import random

secret_number = random.randint(1,10)



guess1 = int(input("Enter your guess (1-10)? "))
guess2 = int(input("Enter your guess (1-10)? "))
guess3 = int(input("Enter your guess (1-10)? "))

if guess1 == secret_number:
    print("You win! The secret number was:", secret_number)
elif guess2 == secret_number:
    print("You win! The secret number was:", secret_number)
elif guess3 == secret_number:
    print("You win! The secret number was:", secret_number)
else:
    print("You lose! The secret number was:", secret_number)