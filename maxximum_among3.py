# Write a function in Python to find the maximum of three numbers.
def maxi(a, b, c):
    large = a
    if b > large:
        large = b
    if c > large:
        large = c
    print(f"Largest of the three is {large}")


a = int(input("enter number1 "))
b = int(input("enter number2 "))
c = int(input("enter number3 "))
maxi(a, b, c)
