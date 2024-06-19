# Factorial calculator

def factorial(n):
    value = 1
    for i in range(1,n+1): # Ensures run from 1 - n inclusive
        value *= i
    return value


try:
    number = int(input("Enter a number: "))
    print(factorial(number))
except ValueError:
    print("Not a number")