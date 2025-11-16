# Question 13: Keep asking for password until correct password is entered

correct_password = "python123"

while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again.")
