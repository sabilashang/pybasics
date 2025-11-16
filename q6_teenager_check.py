# Question 6: Check if age is teenager (13-19) or not

try:
    age = int(input("Enter your age: "))

    if 13 <= age <= 19:
        print("Teenager")
    else:
        print("Not a teenager")
except ValueError:
    print("Error: Please enter a valid age")
