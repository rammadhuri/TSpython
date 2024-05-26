# Write a Python program to check if a number is prime or not using a for loop.

num = int(input("enter a number"))
flag = 0
for i in range(2, int(num**0.5 + 1)):
    if num % i == 0:
        flag = 1
        break
if flag == 1:
    print(f"{num} is not prime")
else:
    print(f"{num} is prime")
