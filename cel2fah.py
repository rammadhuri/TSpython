"""Write a Python program to convert temperature from Celsius to Fahrenheit or 
vice versa based on user input."""


def cel2fah(c):
    f = c * (9 / 5) + 32
    print(f"{c} degree celcius is {f} degree fareheit")


def fah2cel(c):
    c = (f - 32) / (9 / 5)
    print(f"{f} degree celcius is {c} degree fareheit")


c = float(input("enter temp in celcius"))
f = float(input("enter temp in fahrenheit"))
cel2fah(c)
fah2cel(f)
