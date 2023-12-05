# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:59:18 2023

@author: Tristan.Chandler
"""
import sys

shop_name = "virtual coffee maker."
greeting = ("Welcome to the " + shop_name)

print(greeting)

welcome_response = input("")

# Input either hello or goodbye in the prompt above.

welcome_response = welcome_response.lower()

barista = "Joe "
service_question = "what can I get for you? "

if welcome_response == "hello":
    print("My name is " + barista + service_question)
    print("We have 1. Coffee, 2. Tea ~ Enter a number to order. No words, just numbers.")
else:
    welcome_response == "goodbye"
    print("Goodbye have a good day !")
    sys.exit()

# Select 1 or 2 for coffee or tea. No words. Just numbers.
    
selection = int(input("Enter a number here: "))

# Choose any coffee or tea combination when prompted.

if selection == 1:
    print("Coffee what a wonderful selection what kind would you like ?")
    coffee_selection = input("Coffee type: ")
    print(coffee_selection,", awesome that'll be right up.")
elif selection == 2:
    print("Tea what a wonderful choice what kind would you like?")
    tea_selection = input("Tea type: ")
    print(tea_selection, ", awesome that'll be right up.")
else:
    selection == ''
    print("We do not offer that sorry, have a good day !")
    
# If the selection is not offered it will tell you.
# If you select any number aside from 1 or 2, it will not offer anything further.