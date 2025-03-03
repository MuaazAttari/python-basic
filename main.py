name = "Muaaz"   # String
age = 22         # Integer
height = 5.2     # Float
is_student = True  # Boolean

print(name)
print(age)
print(height)
print(is_student)

to_do = ["Eat", "Sleep", "Code", "Repeat"]  # List
cannt_do = ("Lie", "Cheat", "Steal")         # Tuple
when_to_do = {"Eat": "When Hungry", "Sleep": "When Tired", "Code": "When get free"}  # Dictionary

print(type(to_do)) # To check the type of the variable
print(type(cannt_do))
print(type(when_to_do))

# Set........

do_not_repeat = {"Play","use phone","watch TV","use phone"}  # Set

print(do_not_repeat) # Set will not repeat the values
print(type(do_not_repeat))


my_set = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10}  # Set

my_set.add(11) # Add a value in the set
my_set.remove(5) # Remove a value from the set
my_set.discard(6) # Discard a value from the set

print(my_set) # Set will not repeat the values

# Check if the value is in the set or not
print(2 in my_set) # True
print(5 in my_set) # False

# Arithmetic Operators............

a = 10
b = 3

print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication
print(a/b) # Division
print(a//b) # Floor Division  (10 // 3 = 3) -> Removes decimal part
print(a%b) # Modulus  (10 % 3 = 1) -> Gives remainder
print(a**b) # Exponent  (10 ** 3 = 1000) -> 10^3    10*10*10 = 1000

# Comparison Operators............

Num1 = 10
Num2 = 20

print(Num1 == Num2) # False
print(Num1 != Num2) # True
print(Num1 > Num2) # False
print(Num1 < Num2) # True
print(Num1 >= Num2) # False
print(Num1
      <= Num2) # True

# Logical Operators............

x = True
y = False

print(x and y)  # AND -> False (Both must be True)
print(x or y)   # OR  -> True (At least one must be True)
print(not x)   # x = True, but because of not it reverses the value # NOT -> False (Reverses the value)

# Assignment Operators............

num = 5
num += 3  # Same as num = num + 3 (Now num = 8)
num -= 2  # Same as num = num - 2 (Now num = 6)
num *= 4  # Same as num = num * 4 (Now num = 24)
num /= 2  # Same as num = num / 2 (Now num = 12.0)

# Identity Operators............

a = 5
b = 5
c = 10
print(a is b)  # True
print(a is c)  # False
print(a is not c)  # True

# Membership Operators............

fruits = ["Apple", "Banana", "Cherry"]
print("Banana" in fruits)  # True
print("Grapes" not in fruits)  # True
print("Mango" in fruits)  # False

# # All 39 Keywords in Python............

# 1 = False

is_logged_in: bool = False

if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in first.")

# 2 = None

user_name = None

if user_name is None:
    print("No name entered")
else:
    print("Welcome," + user_name)

# 3 = True

accepted_terms = True

if accepted_terms:
    print("Access granted")
else:
    print("You must accept the terms first")

# 4 = And

has_id = True
balance = 500

if has_id and balance >= 500:
    print("Transaction Approved")
else:
    print("Transaction Denied")

# 5 = Or

is_vip = True
balance = 1800

if is_vip or balance >= 1000:
    print("Access granted")
else:
    print("Access denied")

# 6 = Not

is_banned = False

if not is_banned:
    print("You can enter")
else:
    print("Access denied")

# 7 = If

user_score = 50

if user_score >= 50:
    print("You passed")
else:
    print("You failed")

# 8 = Elif

user_age = 10

if user_age >= 18:
    print("you are an adult")
# elif user_age >=13 and user_age <=17:
elif 13 <= user_age <=17:

    print("You are a teenager")
else:
    print("You are a child")

# 9 = while

count = 10

while count >= 1:
    print("Count :",count)
    count -= 1

# 10 = break

count = 1

while count <= 20:
    print("Count :",count)
    if count == 13:
        print("Stopping at 13...")
        break
    count += 1
    
# 11 Continue

count = 1

while count <= 20:
    if count == 10:  # Skip when count is 5
        count += 1  # Increase before skipping
        continue  # Skip this iteration
    
    print("Count:", count)
    count += 1
