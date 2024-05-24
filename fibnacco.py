# Write a Python program to print the Fibonacci series up to n terms using a while loop.
a, b, n = 0, 1, 1
print(a, b, end=" ")
while n <= 10:
    c = a + b
    print(c, end=" ")
    a, b = b, c
    n = n + 1
