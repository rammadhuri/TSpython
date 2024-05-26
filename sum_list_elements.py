# reate a function that takes a list of numbers as input and returns the
#  sum of all the elements.


def sum(lst):
    s = 0
    for i in lst:
        s = s + i
    return s


lst = [1, 3, 10, 8, 3]
summ = sum(lst)
print(f"sum of all the elements is {summ}")
