"""Write a Python program to determine the type of triangle based on the lengths
of its sides (equilateral, isosceles, or scalene)."""


def triangle_type(s1, s2, s3):
    if s1 == s2 == s3:
        print("equilateral traingle")
    elif s1 == s2 or s1== s3 or s2==s3:
        print("isosceles traingle")
    else:
        print("scalene traingle")


s1 = int(input("enter side 1: "))
s2 = int(input("enter side 2: "))
s3 = int(input("enter side 3: "))
triangle_type(s1, s2, s3)
