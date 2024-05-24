# Implement a function to convert a temperature from Celsius to Fahrenheit.
def cel2fah(c):
    f = c * (9 / 5) + 32
    print(f"{c} degree celcius is {f} degree fareheit")


c = float(input("enter temp in celcius"))

cel2fah(c)
