# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

word = input("Enter a word: ")
word = word.lower()

turns = 5

print("Guess the letters:")
print("Num remaining wrong guesses:", turns)

guesses = ''


while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print(", Congratulations!")
        print("The word is:", word)
        break
    print()
    guess = input("Guess a letter:")
    
    guesses += guess
    
    if guess not in word:
        turns -= 1
        print("*" * 30)
        print("Num remaining wrong guesses:", turns)
        if turns == 0:
            print("You Lose!")