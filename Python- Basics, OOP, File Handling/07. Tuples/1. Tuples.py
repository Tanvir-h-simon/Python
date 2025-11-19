# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
print(type(this_tuple))

# Tuples can be of any data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1) 
print(tuple2)
print(tuple3)

mix_tuple = ("abc", 34, True, 40, "male")
print(mix_tuple)

# Tuple items are ordered(indexed), unchangeable, and allow duplicate values.
print(this_tuple[0])
print(this_tuple[1])
print(this_tuple[2])
print(this_tuple[-1])
 # Slicing tuples
print(this_tuple[1:3])

# this_tuple[0] = "mango"
# print(this_tuple)
try:
    this_tuple[0] = "mango"
except:
    print("Tuple is unchangeable")

this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(this_tuple)

# Check if item exists
this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
    print("Yes, 'apple' is in the fruits tuple")

# Lopp through a tuple
this_tuple = ("apple", "banana", "cherry")
for x in this_tuple:
    print(x)
    
this_tuple = ("apple", "banana", "cherry")
for i in range(len(this_tuple)):
    print(this_tuple[i])
    
this_tuple = ("apple", "banana", "cherry")
i = 0
while i < len(this_tuple):
  print(this_tuple[i])
  i = i + 1