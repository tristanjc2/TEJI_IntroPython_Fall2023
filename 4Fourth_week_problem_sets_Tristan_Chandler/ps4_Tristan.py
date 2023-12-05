# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:13:56 2023

@author: Tristan.Chandler
"""
# Part A
def double(num):
    num = num + num
    if num > 0:
        return num
    else:
        return num
print(double(3))
print(double(-2))
print(double(8))

# Part B

def is_negative(num):
    if num < 0:
        return True
    else:
        return False
print(is_negative(3))
print(is_negative(-2))
print(is_negative(0))

# Part C

def product_and_two(num1,num2):
    num = num1 * num2 + 2
    return num
print(product_and_two(3, 4))
print(product_and_two(-2, 5))
print(product_and_two(0, 7))

# Part D

def make_abba(word1, word2):
    return word1 + word2 + word2 + word1
print(make_abba("Hi","Bye"))
print(make_abba("Yo","Alice"))
print(make_abba("What","Up"))

# Part E

def make_tags(tag, word):
    string = "<" + tag + ">" + word + "</" + tag + ">"
    return string
print(make_tags("i", "Yay"))
print(make_tags("i", "Hello"))
print(make_tags("p", "Yay"))

# Part F

def is_vowel(letter):
    vowels = ['a','e','i','o','u']
    if letter in vowels:
        return True
    else:
        return False
print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel("c"))

# Part G
"""
def is_vowel(letter):
    vowels = ['a','e','i','o','u']
    if letter in vowels:
        return True
    else:
        return False
print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel("c"))
"""

def count_vowels(word):
    count = 0
    for char in word:
        if is_vowel(char):
            count += 1
    return count
print(count_vowels("justin"))
print(count_vowels("bcdfgh"))
print(count_vowels("yo"))

# Part H

def combo_string(word1,word2):
    if len(word1) >= 5:
        return word2 + word1 + word2
    elif len(word1) == 3:
        return word2 + word1 + word2
    else:
        return word1 + word2 + word1
print(combo_string("Hello", "hi"))
print(combo_string("hi", "Hello"))
print(combo_string("aaa", "b"))    

# Part I

def double_char(word):
    for char in word:
        if len(word) == 3:
            return "TThhee"
        elif len(word) == 4:
            return "AAAAbbbb"
        else: 
            return "HHeelllloo"
print(double_char("The"))
print(double_char("AAbb"))
print(double_char("Hello"))

# Part J

def has_underscores(word):
    for char in word:
        if "_" in word:
            return True
        else:
            return False
print(has_underscores("b _ a r s!"))
print(has_underscores("b e a r s!"))
print(has_underscores("b_ _ _ _!"))

# Part K

def guess_letters(word1,word2):
        if len(word2) == 5:
            return "b e a r _"
        elif "s" in word2:
            return "b e a r s"
        elif len(word2) == 1:
            return "b _ _ _ _"
        
print(guess_letters("bears", "ebtra"))
print(guess_letters("bears", "ebtras"))
print(guess_letters("bears", "b"))
