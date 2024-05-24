# .Write a Python program to print all even numbers between 1 and 20 using a while loop.
n = 1
while n <= 20:
    if n % 2 == 0:
        print(n, end=" ")
    n = n + 1
