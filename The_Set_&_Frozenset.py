"""📌 What is a Set?
A set in Python is:

Unordered (does not maintain order).
Unindexed (cannot access elements using an index).
Mutable (can be modified).
Unique (does not allow duplicate values).
Defined using curly braces {} or the set() function."""

# Creating a set
fruits = {"Apple", "Banana", "Cherry"}

print(fruits)

# Adding elements to a set
fruits = {"Apple", "Banana"}

fruits.add("Cherry")  # Adding a single item
fruits.update(["Orange", "Mango"])  # Adding multiple items

print(fruits)

# Removing Elements from a Set...

''' We can use:

.remove(item) → Gives an error if item not found.
.discard(item) → No error if item not found.
.pop() → Removes a random item.'''

fruits = {"Apple", "Banana", "Cherry"}

fruits.remove("Banana")  # Removes "Banana"
fruits.discard("Orange")  # No error even if "Orange" is not in the set
popped_item = fruits.pop()  # Removes a random item

print(fruits)
print("Popped:", popped_item)


# Looping through a Set...
fruits = {"Apple", "Banana", "Cherry"}

for fruit in fruits:
    print(fruit)

# Set Operations...
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Union
print(A & B)  # Intersection
print(A - B)  # Difference
print(A ^ B)  # Symmetric Difference

# Check if Item Exists in a Set...

fruits = {"Apple", "Banana", "Cherry"}

if "Apple" in fruits:
    print("Apple is in the set!")

# Finding Length of a Set...
numbers = {10, 20, 30, 40}
print(len(numbers))

# Converting a List to a Set (Removing Duplicates)...
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print(unique_numbers)

"""📌 What is a Frozenset?
A frozenset is:

Immutable (cannot be changed after creation).
Unordered and unique (like a set).
Created using frozenset()."""
# Creating a frozenset...
A = frozenset([1, 2, 3, 4, 5])
print(A)

# Frozenset Operations (Read-Only)...
A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])

print(A | B)  # Union
print(A & B)  # Intersection
print(A - B)  # Difference
print(A ^ B)  # Symmetric Difference
# 📌 Note: A frozenset cannot use .add(), .remove(), or .update().

