# Tuples have very few methods because they are immutable. Only two built-in methods exist
numbers = (1, 2, 3, 2, 2, 4)
print(numbers.count(2))

letters = ("a", "b", "c", "b")
print(letters.index("b"))
# print(letters.index("b", 2)) # Start searching from index 2
try:
    print(letters.index("b", 2))
except:
    print("Not found")