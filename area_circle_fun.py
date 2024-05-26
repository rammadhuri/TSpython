# Develop a function to calculate the area of a circle given its radius.
import math


def area(r):
    return math.pi * math.pow(r, 2)


radii = float(input("enter radius of circle in cm: "))
print(f"area pf circle is {area(radii)} sqcm")
