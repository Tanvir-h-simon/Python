# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable.

# Add elements:
# Tuples are immutable, they do not have a built-in append() method

# Convert into a list: Convert tuple into a list, and convert it back into a tuple
this_tuple = ("apple", "banana", "cherry")
this_list = list(this_tuple)
this_list.append("orange")
this_tuple = tuple(this_list)
print(this_tuple)

# Add tuple to a tuple:
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("orange",)
tuple1 += tuple2
print(tuple1)

# Multiply tuples:
fruits = ("apple", "banana", "cherry")
this_tuple = fruits * 2
print(this_tuple)

numbers = (1, 2, 3, 4, 5)
this_tuple = numbers * 2
print(this_tuple)

# Remove elements:
# Tuples are unchangeable, so we cannot remove items from it, but we can use the same workaround as we used for changing and adding tuple items

# Convert into a list:
this_tuple = ("apple", "banana", "cherry")
this_list = list(this_tuple)
this_list.remove("apple")
this_tuple = tuple(this_list)
print(this_tuple)

# Delete tuple:
this_tuple = ("apple", "banana", "cherry")
del this_tuple
# print(this_tuple) # This will raise an error because the tuple no longer exists
try:
    print(this_tuple)
except NameError:
    print("Already deleted")
    