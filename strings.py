"""
message = "A kong string with a silly typo"

new_message = message[0:2] + "l" + message[3:]
print(new_message)
"""
"""
pets = "Cats & Dogs"
pets.index("&")
# Returns 5
# Cats in pets
# Returns "True"
"""
"""
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
"""
"""
" yes ".strip()
" yes ".lstrip()
" yes ".rstrip()

"Forest".endswith("rest")
# Returns True
"Forest".isnumeric()
# Returns False
"12345".isnumeric()
# Returns True, Even though it's in a string.
# Can use int() to convert string of numbers to actual int.
int("12345") + int ("54321")

# Joins strings with what's in the first sting 
" ".join(["This","is","a","phrase","joined","by","spaces"])

"...".join(["This","is","a","phrase","joined","by","triple","dots"])

# Splits a string in a list format.
# Can split strings with a comma or a dot.
"This is another example".split()
"""
"""
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
# prints 7.5, 8.175
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
"""
"""
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print('{:>3} F | {:>6.2f} C'.format(x, to_celsius(x)))
"""
"""
String operations -

len(string) - Returns the length of the string

for character in string - Iterates over each character in the string

if substring in string - Checks whether the substring is part of the string

string[i] - Accesses the character at index i of the string, starting at zero

string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted, its value defaults to 0. If j is omitted, the value will default to len(string).

String methods
string.lower() - Returns a copy of the string with all lowercase characters

string.upper() - Returns a copy of the string with all uppercase characters

string.lstrip() - Returns a copy of the string with the left-side whitespace removed

string.rstrip() - Returns a copy of the string with the right-side whitespace removed

string.strip() - Returns a copy of the string with both the left and right-side whitespace removed

string.count(substring) - Returns the number of times substring is present in the string

string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.

string.isalpha() - Returns True if there are only alphabetic characters in the string. If not, returns False.

string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)

string.split(delimiter) - Returns a list of substrings that were separated by whitespace or a delimiter

string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.

delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter 
"""


