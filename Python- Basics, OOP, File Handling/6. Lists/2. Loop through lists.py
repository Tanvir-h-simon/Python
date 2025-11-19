this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x, end=" ")
print()    

# Loop Through the Index Numbers
for i in range(len(this_list)):
    print(this_list[i], end=" ")
print()
    
# Using a while loop
i = 0
while i < len(this_list):
    print(this_list[i], end=" ")
    i = i + 1
print()

# List Comprehension (List comprehension offers a shorter syntax when we want to create a new list based on the values of an existing list).
# List comprehension is a concise and elegant way to create lists in a single line, instead of using loops.
# It makes your code shorter, faster, and more readable.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = []
# for x in fruits:
#     if "a" in x:
#         new_list.append(x)
# print(new_list)
new_list = [x for x in fruits if "a" in x] # new_list = [expression for item in iterable]
print(new_list)

numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(result)

newlist = [x for x in range(10) if x < 5]
print(newlist)

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)

text = "Python"
letters = [ch.upper() for ch in text]
print(letters)

matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)