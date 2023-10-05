import math
import cmath
import os

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def exponent(x, y):
    return x ** y

def squareroot(x):
    return math.sqrt(x)

def log(x, y):
    return cmath.log(x, y)

def ln(x):
    return math.log(x)

def remainder(x,y):
    return x % y
def clear():
    return os.system('cls')


    




print("What Operation?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponents")
print("6. Squareroot")
print("7. Log")
print("8. ln")
print("9. Remainder")
print("10. Clear")

while True:
    choice = input("Pick 1,2,3,4,5,6,7,8,9,10")

    if choice in ('1', '2', '3', '4', '5', '9'):
        try: 
            x = float(input("What is the first number?"))
            y = float(input("What is the second number?")) 
        except ValueError:
            print("Please enter valid number")

        if choice == '1':
            print(add(x, y))
        if choice == '2':
            print(subtract(x, y))
        if choice == '3':
            print(multiply(x, y))
        if choice == '4':
            print(divide(x, y))
        if choice == '5':
            print(exponent(x, y))


        if choice == '9':
            print(remainder(x, y))

    if choice in ('6', '8'):
        try: 
            x = float(input("What is the number?"))
        except ValueError:
            print("Please enter valid number")

        if choice == '6':
            print(squareroot(x))

        if choice == '8':
            print(ln(x))

    if choice in ('7'):
        try: 
            x = float(input("What is the base?"))
            y = float(input("What is a?"))
        except ValueError:
            print("Please enter valid number")

        if choice == '7':
            print(log(x, y))

    if choice == "10":
        print(clear())