import time
import sys

count = 0

question1 = "What is the capitol of the United States?"
answer1 = "A) New York \nB) Washington DC \nC) Boston \nD) San Francisco"
question1_hint = ""

question2 = "Which of the following is NOT a fruit?"
answer2 = "A) Rhubarb \nB) Tomatoes \nC) Avocados \nD) Apple"
question2_hint = ""

question3 = "Who is generally considered the inventor of the motor car?"
answer3 = "A) Henry Ford \nB) Karl Benz \nC) Henry M. Leland \nD) Dodge Mills"
question3_hint = ""

question4 = "What number was the Apollo mission that successfully put a man on the moon for the first time in human history?"
answer4 = "A) Apollo 11 \nB) Apollo 12 \nC) Apollo 13 \nD) Apollo 16"
question4_hint = ""

question5 = "Which of the following languages has the longest alphabet?"
answer5 = "A) English \nB) Greek \nC) Russian \nD) Arabic"
question5_hint = ""

question6 = "What spirit is used in making a Tom Collins?"
answer6 = "A) Vodka \nB) Rum \nC) Gin \nD) Brandy"
question6_hint = ""

question7 = "The fear of insects is known as what?"
answer7 = "A) Entomophobia \nB) Arachnophobia \nC) Ailurophobia \nD) Aphobia"
question7_hint = ""

question8 = "What is the largest US state (by landmass)?"
answer8 = "A) Texas \nB) Alaska \nC) California \nD) Maine"
question8_hint = ""

question9 = "Which app has the most total users?"
answer9 = "A) TikTok \nB) Snapchat \nC) Instagram \nD) Twitter"
question9_hint = ""

question10 = "How many plays do people (generally) believe that Shakespeare wrote?"
answer10 = "A) 27 \nB) 37 \nC) 47 \nD) 100"
question10_hint = ""

print("Wanna be a millionaire ?")
time.sleep(0.5)

print(question1)
time.sleep(0.5)
print(answer1)
time.sleep(0.5)
answer = str(input("Enter A, B, C or D: "))
answer = answer.lower()
if answer == "b":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 1:
        print("You won 1$ !")
        time.sleep(0.5)
        print("Would you like to continue? (yes or no)")
        proceed = input("Enter yes or no: ")


if proceed == "yes":
    print(question2)
    time.sleep(0.5)
    print(answer2)
    answer = str(input("Enter A, B, C or D: "))
    answer = answer.lower()
if answer == "a":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 2:
        print("You won 100$ !")
        time.sleep(0.5)
        print("Would you like to continue? (yes or no)")
        proceed = input("Enter yes or no: ")


if proceed == "yes":
    print(question3)
    time.sleep(0.5)
    print(answer3)
    answer = str(input("Enter A, B, C or D: "))
    answer = answer.lower()
if answer == "b":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 3:
        print("You won 500$ !")
        time.sleep(0.5)
        print("Would you like to continue? (yes or no)")
        proceed = input("Enter yes or no: ")


if proceed == "yes":
    print(question4)
    time.sleep(0.5)
    print(answer4)
    answer = str(input("Enter A, B, C or D: "))
    answer = answer.lower()
if answer == "a":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 4:
        print("You won 1,000$ !")
        time.sleep(0.5)
        print("Would you like to continue? (yes or no)")
        proceed = input("Enter yes or no: ")


if proceed == "yes":
    print(question5)
    time.sleep(0.5)
    print(answer5)
    answer = str(input("Enter A, B, C or D: "))
    answer = answer.lower()
if answer == "c":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 5:
        print("You won 10,000$ !")
        time.sleep(0.5)
        print("Would you like to continue? (yes or no)")
        proceed = input("Enter yes or no: ")


if proceed == "yes":
    print(question6)
    time.sleep(0.5)
    print(answer6)
    answer = str(input("Enter A, B, C or D: "))
    answer = answer.lower()
if answer == "c":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 6:
        print("You won 50,000$ !")
        time.sleep(0.5)
        print("Would you like to continue? (yes or no)")
        proceed = input("Enter yes or no: ")


if proceed == "yes":
    print(question7)
    time.sleep(0.5)
    print(answer7)
    answer = str(input("Enter A, B, C or D: "))
    answer = answer.lower()
if answer == "a":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 7:
        print("You won 100,000$ !")
        time.sleep(0.5)
        print("Would you like to continue? (yes or no)")
        proceed = input("Enter yes or no: ")


if proceed == "yes":
    print(question8)
    time.sleep(0.5)
    print(answer8)
    answer = str(input("Enter A, B, C or D: "))
    answer = answer.lower()
if answer == "b":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 8:
        print("You won 250,000$ !")
        time.sleep(0.5)
        print("Would you like to continue? (yes or no)")
        proceed = input("Enter yes or no: ")


if proceed == "yes":
    print(question9)
    time.sleep(0.5)
    print(answer9)
    answer = str(input("Enter A, B, C or D: "))
    answer = answer.lower()
if answer == "c":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 9:
        print("You won 500,000$ !")
        time.sleep(0.5)
        print("Would you like to continue? (yes or no)")
        proceed = input("Enter yes or no: ")


if proceed == "yes":
    print(question10)
    time.sleep(0.5)
    print(answer10)
    answer = str(input("Enter A, B, C or D: "))
    answer = answer.lower()
if answer == "b":
    print("Correct!")
    count += 1
else:
    print("Sorry, you lose!")
    sys.exit("")
if count == 10:
        print("You won 1,000,000$ !")
        time.sleep(0.5)
        print("You won the game! Thanks for playing !")


