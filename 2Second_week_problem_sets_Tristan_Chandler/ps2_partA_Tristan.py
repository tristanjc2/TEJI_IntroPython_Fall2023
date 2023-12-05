# -*- coding: utf-8 -*-
grade_1 = int(input("What was the grade on exam 1? "))
grade_2 = int(input("What was the grade on exam 2? "))
grade_3 = int(input("What was the grade on exam 3? "))

average_grade = (grade_1 + grade_2 + grade_3)
average_grade = average_grade/3

if average_grade >= 90:
    print("You got an A")
elif average_grade >= 80:
    print("You got a B")
elif average_grade >= 70:
    print("You got a C")
elif average_grade >= 60:
    print("You got a D")
else: 
    print("You got an F")
    
