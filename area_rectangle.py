"""Write a Python program to calculate the area of a rectangle using the
 length and width provided by the user.
 """


def area(l, b):
    return l * b


length = float(input("enter length of rectangle in cm"))
width = float(input("enter width of rectangle in cm"))
ar = area(length, width)
print(f"Area of the rectangle having {length}cm and {width}cm is {ar} square cm.")
