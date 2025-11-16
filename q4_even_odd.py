# Question 4: Check whether a number is even or odd

try:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
except ValueError:
    print("Error: Please enter a valid integer")
