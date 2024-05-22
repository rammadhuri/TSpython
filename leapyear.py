# Write a Python program to check if a year entered by the user is a leap year or not.


def leap(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print(f"{y} is Leap year ")
    else:
        print(f"{y} is not a Leap year ")


year = int(input("enter year"))
leap(year)
