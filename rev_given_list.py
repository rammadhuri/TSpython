# Write a Python program to reverse a list using a while loop.
res = list()
lst = [1, 2, 8, 6, 4]
n = len(lst)
while n > 0:
    res.append(lst[n - 1])
    n = n - 1
print(res)
