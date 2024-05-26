# Write a function that takes a list of integers as input and returns the product
# of all the elements.


def e_product(lst):
    p = 1
    for i in lst:
        p = p * i
    return p


lst = [2, 3, 10, 8, 3]
print(f"sum of all the elements is {e_product(lst)}")
