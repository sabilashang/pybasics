# Question 14: Check whether a given year is a leap year or not

try:
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
except ValueError:
    print("Error: Please enter a valid year")
