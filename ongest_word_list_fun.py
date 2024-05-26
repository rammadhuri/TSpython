# Develop a function that takes a list of words as input and returns the longest word.
def longest(lst):
    long = len(lst[0])
    ele = lst[0]
    for word in lst:
        if len(word) > long:
            long = len(word)
            ele = word
    return ele


lst = ["anny", "harry", "madhur", "charlesIV"]
print(f"longest of all the elements is {longest(lst)}")
