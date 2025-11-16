# Question 1: Check whether a number is positive, negative, or zero

try:
    number = float(input("Enter a number: "))

    if number > 0:
        print("The number is positive")
    elif number < 0:
        print("The number is negative")
    else:
        print("The number is zero")
except ValueError:
    print("Error: Please enter a valid number")
