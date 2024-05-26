"""Write a Python program to check if a character entered by the user is a vowel, 
consonant, or neither  using conditional statements."""


def classification(ch):
    if len(ch) != 1:
        print("Please enter single character")
        return
    vowel = ["a", "i", "e", "o", "u", "A", "I", "O", "E", "U"]
    if ch in vowel:
        print(f"{ch} is vowel")
    elif "a" < ch < "z" and "A" < ch < "Z":
        print(f"{ch} is Consonant")
    else:
        print(f"{ch} is neither consonant nor vowel")


letter = input("enter a character ")
classification(letter)
