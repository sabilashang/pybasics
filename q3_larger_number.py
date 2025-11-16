# Question 3: Take two numbers and print the larger one using if statement

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num1 > num2:
        print(f"The larger number is: {num1}")
    elif num2 > num1:
        print(f"The larger number is: {num2}")
    else:
        print("Both numbers are equal")
except ValueError:
    print("Error: Please enter valid numbers")
