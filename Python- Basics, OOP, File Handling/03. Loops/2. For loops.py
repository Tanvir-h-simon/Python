# Looping through a string
for x in "banana":
    print(x)

# The range() Function: range(start, stop, step)- starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)
    
for x in range(2, 30, 3): # Third parameter -> Increment (Default is 1)
    print(x)

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
    
# Else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# The pass statement
for x in [0, 1, 2]:
    pass