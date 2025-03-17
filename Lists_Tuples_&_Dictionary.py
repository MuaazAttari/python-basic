""" Lists are used to store multiple items in a single variable.
    Lists are created using square brackets.
    There are several ways to create a list in Python."""

# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["Apple", "Banana", "Cherry"]

# Mixed data types
mixed_list = [10, "Python", 3.14, True]

print(numbers)
print(fruits)
print(mixed_list)

# Accessing List Elements
# List indexing starts from 0

fruits = ["Apple", "Banana", "Cherry"]

print(fruits[0])  # First element
print(fruits[1])  # Second element
print(fruits[-1]) # Last element (Negative Indexing)

# Modify List Elements

fruits = ["Apple", "Banana", "Cherry"]
fruits[1] = "Mango"  # Changing "Banana" to "Mango"
print(fruits)

# Add Elements to a List...

fruits = ["Apple", "Banana"]
fruits.append("Cherry")  # Adds "Cherry" at the end
fruits.insert(1, "Mango")  # Inserts "Mango" at index 1

print(fruits)

# Remove Elements from a List

fruits = ["Apple", "Banana", "Cherry"]

fruits.remove("Banana")  # Removes "Banana"
fruits.pop(1)  # Removes item at index 1 (Cherry)
del fruits[0]  # Deletes "Apple"

print(fruits)  # Empty list now

# Loop Through a List

fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit)

# Check if Item Exists

fruits = ["Apple", "Banana", "Cherry"]

if "Banana" in fruits:
    print("Yes, Banana is in the list!")

# Sort a List

numbers = [5, 2, 8, 1, 4]

numbers.sort()  # Sorts in ascending order
print(numbers)

numbers.sort(reverse=True)  # Sorts in descending order
print(numbers)


# Copy a List

original_list = ["A", "B", "C"]
copy_list = original_list.copy()

copy_list.append("D")

print("Original:", original_list)
print("Copy:", copy_list)


# List Comprehension (Shorter way to create lists)

# Generate a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)


""" 📌 What is a Tuple?
    A tuple in Python is:

    Ordered (maintains the order of elements).
    Immutable (cannot be changed after creation).
    Allows duplicate values.
    Defined using parentheses ().
    Tuples are similar to lists but are immutable.
    Tuples are created using parentheses.
    There are several ways to create a tuple in Python."""
    
# We can create a tuple by placing elements inside ().

# Tuple of numbers
numbers = (1, 2, 3, 4, 5)

# Tuple of strings
fruits = ("Apple", "Banana", "Cherry")

# Mixed data types
mixed_tuple = (10, "Python", 3.14, True)

print(numbers)
print(fruits)
print(mixed_tuple)

# Accessing Tuple Elements...

fruits = ("Apple", "Banana", "Cherry")

print(fruits[0])  # First element
print(fruits[1])  # Second element
print(fruits[-1]) # Last element (Negative Indexing)

# Slice a Tuple

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])  # Elements from index 1 to 3
print(numbers[:3])   # First 3 elements
print(numbers[3:])   # From index 3 to end
print(numbers[-3:])  # Last 3 elements

# Looping Through a Tuple

fruits = ("Apple", "Banana", "Cherry")

for fruit in fruits:
    print(fruit)

# Tuple Unpacking...

colors = ("Red", "Green", "Blue")
x, y, z = colors

print(x)
print(y)
print(z)

# Check if Item Exists

fruits = ("Apple", "Banana", "Cherry")

if "Banana" in fruits:
    print("Yes, Banana is in the tuple!")

# Find Length of a Tuple...

fruits = ("Apple", "Banana", "Cherry")
print(len(fruits))

# Concatenating (Joining) Tuples...
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2
print(result)

# Converting Tuple to List (for Modification)
fruits = ("Apple", "Banana", "Cherry")
fruits_list = list(fruits)  # Convert to list

fruits_list.append("Mango")  # Add a new item
fruits = tuple(fruits_list)  # Convert back to tuple

print(fruits)

# Counting and Finding Index in Tuples

numbers = (1, 2, 3, 2, 4, 2)

print(numbers.count(2))  # Count occurrences of 2
print(numbers.index(4))  # Find index of 4


'''📌 What is a Dictionary?
    A dictionary in Python is:

    Unordered (does not maintain the order of elements).
    Mutable (can be changed after creation).
    Indexed (accessed by keys).
    Defined using curly braces {}.
    Keys must be unique, but values can be duplicated.
    Dictionaries are used to store key-value pairs.
    There are several ways to create a dictionary in Python.'''
    
# We can create a dictionary by placing key-value pairs inside {}.

# Creating a dictionary
student = {
    "name": "Muaaz",
    "age": 22,
    "city": "Hyderabad"
}

print(student)

# Accessing Dictionary Values...

student = {
    "name": "Muaaz",
    "age": 22,
    "city": "Hyderabad"
}

print(student["name"])  # Accessing "name"
print(student.get("age"))  # Accessing "age" using get()


# Modifying Dictionary Values...
student = {
    "name": "Muaaz Ansari",
    "age": 22,
    "city": "Hyderabad"
}

# Modifying value
student["age"] = 23

# Adding a new key-value pair
student["course"] = "Python"

print(student)

#  Removing Items from a Dictionary.
'''We can remove items using:

.pop(key) → Removes specific key.
del → Deletes a key.
.popitem() → Removes the last key-value pair.'''

student = {
    "name": "Muhammad Muaaz",
    "age": 22,
    "city": "Hyderabad"
}

student.pop("age")  # Removes "age"
del student["city"]  # Removes "city"
print(student)

# Loop Through a Dictionary...

student = {
    "name": "Muaaz",
    "age": 22,
    "city": "Hyderabad"
}

# Looping through keys
for key in student:
    print(key)

# Looping through values
for value in student.values():
    print(value)

# Looping through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")


#  Checking If a Key Exists...
# We can use the in keyword.
student = {
    "name": "Ali",
    "age": 32,
    "city": "Hyderabad"
}

if "age" in student:
    print("Age is present in the dictionary")

# Dictionary Length...
student = {
    "name": "Mohsin",
    "age": 28,
    "city": "Hyderabad"
}

print(len(student))

# Copy a Dictionary.
# We can copy a dictionary using the copy() method.
student = {
    "name": "Areeba",
    "age": 22
}

copy_student = student.copy()
copy_student["age"] = 25  # Only changes copy

print("Original:", student)
print("Copy:", copy_student)

# Nested Dictionaries...
# We can have a dictionary inside another dictionary.
students = {
    "student1": {"name": "Muaaz", "age": 22},
    "student2": {"name": "Ayesha", "age": 20}
}

print(students["student1"]["name"])  # Accessing nested value

# Dictionary Comprehension (Shortcut to Create Dictionaries)
# We can use dictionary comprehension to create dictionaries.
# Creating a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)
