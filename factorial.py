# Write a Python program to calculate the factorial of a number entered by the user.


def factorial(n):
    fact = 1
    num = n
    while n > 0:
        fact = fact * n
        n = n - 1
    print(f"Factoial of {num} is {fact}")


num = int(input("enter the number"))
factorial(num)
