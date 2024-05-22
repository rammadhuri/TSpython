# Write a Python program to determine the grade of a student based on
# their percentage score(A for 90% or above, B for 80% to 89%, etc.).

g1 = int(input("Enter marks of  subject1: "))
g2 = int(input("Enter marks of  subject2: "))
g3 = int(input("Enter marks of subject3: "))
g4 = int(input("Enter marks of  subject4: "))
g5 = int(input("Enter marks of subject5: "))
sum = g1 + g2 + g3 + g4 + g5
per = (sum / 500) * 100
print(f"percentage:{per}%")
if per >= 90:
    print("Grade: A")
elif per >= 80 and per < 90:
    print("Grade: B")
elif per >= 70 and per < 80:
    print("Grade: C")
elif per >= 60 and per < 70:
    print("Grade: D")
else:
    print("Grade: F")
