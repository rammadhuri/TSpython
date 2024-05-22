# Write a Python program to determine the roots of a quadratic
# equation entered by the user using conditional statements.

import math


def find_roots(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"root 1: {root1}")
        print(f"root 2: {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"root:{root}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        print(f"root 1:{real_part}+{imaginary_part} i")
        print(f"root 2:{real_part}-{imaginary_part} i")


print("Quadratic Equation: ax^2 + bx + c = 0")
a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    find_roots(a, b, c)
