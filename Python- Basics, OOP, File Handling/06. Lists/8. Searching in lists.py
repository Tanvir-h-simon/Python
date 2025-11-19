# Searching in list
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
# print(fruits.index("mango")) # Returns index of first occurrence of x. Raises error if not found.
try:
    print(fruits.index("apple"))
except ValueError:
    print("Item not found.")   
# try:
#     print(fruits.index("jackfruit"))
# except ValueError:
#     print("Item not found.")

# Search within a specific range
numbers = [10, 20, 30, 20, 40, 20]
print(numbers.index(20, 1, 5)) # Search for 20 only between index 1 and 5
print(numbers.index(40, 0, 5))  # Search for 40 between index 0 and 5
print(numbers.index(20, 2))  # Start from index 2 → 3
print(numbers.index(20, 4))  # Start from index 4 → 5

# Counting elements in list
fruits = ["apple", "banana", "cherry", "banana", "kiwi"]
print(fruits.count("banana")) # Counts how many times x appears in the list.

words = ["Apple", "apple", "APPLE"]
print(words.count("apple"))

nums = [1, 2, 2, 3, 4, 2, 5]
print(nums.count(2))