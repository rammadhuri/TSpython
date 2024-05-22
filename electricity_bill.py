"""Write a Python program to calculate the electricity bill for a user based on
 the units consumed using conditional statements (consider different slab rates)."""


def bill(units):
    if units <= 50:
        bill = units * 0.50
    elif units <= 150:
        bill = 50 * 0.50 + (units - 50) * 0.75
    elif units <= 250:
        bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
    else:
        bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50
    return bill


units_consumed = float(input("Enter the units consumed: "))
if units_consumed < 0:
    print("Invalid input. Units consumed cannot be negative.")
else:
    bill_amount = bill(units_consumed)
    print(f"Electricity Bill:{bill_amount}")
