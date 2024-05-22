"""Write a Python program to determine the eligibility of a candidate for 
voting based on their age (18 years or older)"""


def vote(age):
    if age >= 18:
        print("You can Vote")
    else:
        print("You cannot Vote")


age = int(input("Enter your age : "))
vote(age)
