# Question 11: Print multiplication table of a number

try:
    number = int(input("Enter a number: "))

    print(f"\nMultiplication table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
except ValueError:
    print("Error: Please enter a valid integer")
