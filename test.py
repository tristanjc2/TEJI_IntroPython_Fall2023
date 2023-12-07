# Classes Warrior, Mage, Ninja
"""
class Characters:
    health = 100
    height = []
    weight = []
    race = ""
    role = ""

warrior = Characters()
warrior.height = 6.0
warrior.weight = 200
warrior.race = "human"
warrior.role = "warrior"

mage = Characters()
mage.height = 5.0
mage.weight = 160
mage.race = "human"
mage.role = "mage"

ninja = Characters()
ninja.height = 5.5
ninja.weight = 155
ninja.race = "human"
ninja.role = "ninja"
"""
"""
class Apple:
    pass
    # pass means the body is empty

class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"

class Bird:
    color = ""
    number = 0

bluejay = Bird()
bluejay.number = 20
print(bluejay.number)
"""
"""
class Piglet:
    # Need years declared to run pig_years()
    years = 0
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))
    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())
"""
"""
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

jonagold = Apple("red", "sweet")

print(jonagold.color)
"""
"""
class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor 
    def __str__(self):
        return "The apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red","sweet")
"""

# class Piglet:
#     """Represents a piglet that can say their name."""
#     years = 0
#     name = ""
#     def speak(self):
#         """Outputs a message including the name of the piglet."""
#         print("Oink! I'm {}! Oink!".format(self.name))
#     def pig_years(self):
#         """Converts the current age to equivalent pig years."""
#         return self.years * 18
#     help(speak) #needs to be on the same indent as the def method.
"""
class Fruit:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
print(carnelian.flavor)
"""
"""
class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "Moooooo"

milky = Cow("Milky White")
milky.speak()
"""

class Repository:
    def __init__(self):
        self.packages = {}
    def add_packages(self, package):
        self.packages[package.name] = package
    def remove_packages(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.package.values():
            result += package.size
        return result
