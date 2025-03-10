# # Arithmetic Operators
print(" ============== Arithmetic operators  ============")

money_i_have = 100
product_cost = 30

print(money_i_have + product_cost) # 100 + 30 = 130
print(money_i_have - product_cost) # 100 - 30 = 70
print(money_i_have * product_cost) # 100 * 30 = 3000
print(money_i_have / product_cost) # 100 / 30 = 3.3333333333333335
print(money_i_have // product_cost) # 100 // 30 = 3
print(money_i_have % product_cost) # 100 % 30 = 10
print(money_i_have ** product_cost) # 100 ** 30 = 100
print("===============================================")

# # Assignment Operators
print(" ============== Assignment operators  ============")
x = 5
x += 3
x -= 3
x *= 3
x /= 3
x %= 3
x //= 3
x **= int(3)

# x &= 3
# x |= 3
# x ^= 3
# x >>= 3
# x <<= 3

print(x)
print("===============================================")

# # Comparison Operators
print(" ============== Comparison operators  ============")

x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True
print("===============================================")

# # Logical Operators

print(" ============== Logical operators  ============")

oil_in_biryani = True
oil_in_drink = False

print(oil_in_biryani and oil_in_drink)  # False
print(oil_in_biryani or oil_in_drink)  # True
print(not oil_in_biryani)  # False
print(not oil_in_drink)  # True
print("===============================================")

# # Identity Operators

print(" ============== Identity operators  ============")

""" Identity operators are used to compare the objects, not if they are equal,
    but if they are actually the same object, with the same memory location:"""
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
print(a is not c)  # True
print("===============================================")

# # Membership Operators

print(" ============== Membership operators  ============")

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("mango" not in fruits)  # True
print("mango" in fruits)  # False
print("===============================================")

# # Bitwise Operators....

print(" ============== Bitwise operators  ============")

""" Bitwise operators are used to perform operations at the binary level.
    They work directly on bits and are useful for optimizing performance in low-level programming,
    cryptography, and data compression."""

x = 5  # 0101 in binary
y = 3  # 0011 in binary

print(x & y)  # 1  (0001)
print(x | y)  # 7  (0111)
print(x ^ y)  # 6  (0110)
print(~x)     # -6 (Negative of 5 + 1)
print(x << 1) # 10 (1010)
print(x >> 1) # 2  (0010)
print("===============================================")



