# Write a function to reverse a given list.
def rev(lst):
    res = []
    for i in range(len(lst) - 1, -1, -1):
        res.append(lst[i])
    print(res)


lst = [1, 2, 3, 45, 8, 34]
rev(lst)
