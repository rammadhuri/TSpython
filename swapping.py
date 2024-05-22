# Write a Python program to swap the values of two variables without using a temporary variable.
# Method1
def swap1(a, b):
    a, b = b, a
    print(f"after swapping:a={a} and b={b}")


# Method2
def swap2(a, b):
    a = a + b
    b = a - b
    a = a - b
    print("after swapping:a={a} and b={b}")


a = int(input("enter a"))
b = int(input("enter b"))
print(f"before swapping: a={a} and b={b}")
swap1(a, b)
swap2(a, b)
