# Even or Odd checker
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# Grade calculator....

marks = int(input("Enter your marks: "))
if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# For loop to print multiplication table of a number

num = int(input("Enter a number to create a Table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# While Loop Example: Countdown Timer

count = int(input("Enter countdown start number: "))

while count > 0:
    print(count)
    count -= 1

print("Time's up!")


# Break Example: Stop Loop at a Specific Condition


for i in range(1, 10):
    if i == 5:
        print("Loop stopped at 5")
        break
    print(i)


# Continue Example: Skip even numbers

for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)


# Nested Loop Example: Right-Angle Triangle Pattern

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Sum numbers from 1 to 100
total: int = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)