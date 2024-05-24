# Write a Python program to calculate the factorial of a number using a for loop.
n = int(input("enter a number "))
fact = 1
for i in range(2, n + 1):
    fact = fact * i
print(f"the factorial of a {n}is {fact}")
