"""
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)
"""
"""
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0,"Orange")
print(fruits)

fruits.remove("Melon")
print(fruits)

fruits.pop(3)
print(fruits)

fruits[2] = "Strawberry"
"""
"""
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0 
for animal in animals:
    chars += len(animals)
print("Total Characters: {}, Average Length: {}".format(chars, chars/len(animals)))
"""
"""
winners = ["Ashley", "Dillion", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
"""
"""
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result
print(full_emails([("Alex@example.com", "Alex Diego"), ("Shay@example.com", "Shay Brandt")]))
"""
"""
multipules = []
for x in range(1,11):
    multipules.append(x*7)
print(multipules)
"""
"""
multipules = [ x*7 for x in range(1,11)]
print(multipules)
"""
"""
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(languages)
"""
"""
z = [x for x in range(1,101) if x % 3 == 0]
print(z)
"""
