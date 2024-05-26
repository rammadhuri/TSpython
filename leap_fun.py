# Implement a function to check if a given year is a leap year or not.
def leapyr(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    return False


year = int(input("enter the year"))
l = leapyr(year)
if l:
    print("Leap year")
else:
    print("not leap year")
