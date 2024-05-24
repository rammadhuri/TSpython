# Write a Python program to find the largest number in a list using a for loop.
arr = [2, 98, 6, 167, 334, 98, 36]
maxx = arr[0]
for i in arr:
    if i > maxx:
        maxx = i
print(f"the largest number in a list  is {maxx}")
