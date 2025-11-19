# Lists are used to store multiple items in a single variable.
# Pyhthon has 4 built-in data types used to store collections of data: List, Tuple, Set, and Dictionary
''' Python Collections (Arrays)
There are four collection data types in the Python programming language: 
1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
this_list = ["apple", "banana", "cherry"] 
print(this_list)
print(type(this_list))

# List items can be of any data type:
odd_number = [1, 3, 5, 7, 9]
print(odd_number)
boolean_list = [True, False, True]
print(boolean_list)
mixed_list = ["abc", 34, True, 40, "male"]
print(mixed_list)

# Access list items:
print(this_list[0])
print(this_list[1])
print(this_list[-1]) # Negative indexing means start from the end
# Range of indexes:
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])
print(this_list[:4])
print(this_list[2:])
print(this_list[-4:-1])
this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list)

# List items are ordered(indexed), changeable, and allow duplicate values.
this_list[0] = "mango"
this_list[2] = "mango"
print(this_list)

# Check if item exists
this_list = ["apple", "banana", "cherry"] 
if "apple" in this_list:
    print("Yes, 'apple' is in the fruits list")