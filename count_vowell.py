# Write a Python program to count the number of vowels in a string using a for loop.
count = 0
vowel = ["a", "i", "o", "u", "e"]
strng = input("enter string")
for ch in strng:
    if ch in vowel:
        count += 1
print(f"count the number of vowels is {count}")
