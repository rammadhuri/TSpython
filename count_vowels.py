# Create a function that takes a string as input and returns the number of vowels in it.
def count(strn):
    vowel = ["a", "i", "o", "u", "e"]
    count = 0
    s = strn.lower()
    for ch in s:
        if ch in vowel:
            count += 1
    return count


strn = input("enter string")
x = count(strn)
print(f"count the number of vowels is {x}")
