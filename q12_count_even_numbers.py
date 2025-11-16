# Question 12: Count how many even numbers are between 1 and 50

count = 0
for i in range(1, 51):
    if i % 2 == 0:
        count += 1

print(f"There are {count} even numbers between 1 and 50")
