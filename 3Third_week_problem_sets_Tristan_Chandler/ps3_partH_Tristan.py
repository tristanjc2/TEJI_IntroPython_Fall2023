# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:10:38 2023

@author: Tristan.Chandler
"""

import random

#random_move = random.choice(["rock","paper","scissors"])


#choice = str(input("Enter rock, paper or scissors: "))


win = 0
loss = 0
tie = 0

for i in range(5):
    choice = str(input("Enter rock, paper or scissors: "))
    random_move = random.choice(["rock","paper","scissors"])
    #while choice == random_move:
     #   print("You tied!")
      #  tie += 1
       # break
    if choice == 'rock' and random_move == 'paper':
        print("You lose!")
        loss += 1
    elif choice == 'rock' and random_move == 'scissors':
        print("You win!")
        win += 1
    elif choice == 'paper' and random_move == 'rock':
        print('You win!')
        win += 1
    elif choice == 'paper' and random_move == 'scissors':
        print('You lose!')
        loss +=1
    elif choice == 'scissors' and random_move == 'paper':
        print('You win!')
        win += 1
    elif choice == 'scissors' and random_move == 'rock':
        print('You lose!')
        loss +=1
    else:
        print("You tied!")
        tie += 1
print()
print("You won", win, "time(s)")
print("You lost", loss, "time(s)")
print("You tied", tie, "time(s)")

