# Tuple constructor
# tuple(iterable): Converts an iterable to tuple.
print(tuple("abc"))
# word = tuple("abc")
# print(word)
word = tuple(["abc", "Hello"]) # Square brackets: Convert list to tuple
print(word)
fruits = tuple(["apple", "banana", "cherry"])
print(fruits)


fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Tuple length
print(len(fruits))

# Tuple sum
number = (1, 2, 3, 4, 5)
print(sum(number))

# Tuple maximum
print(max(number))

# Tuple minimum
print(min(number))

# 2D tuples:
matrix = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)
# Length of matrix (number of rows)
print(len(matrix))
# Length of a specific row
print(len(matrix[0]))
print(len(matrix[1]))
# Sum for each row
for i, row in enumerate(matrix):
    print(sum(row))
# Find total sum
total_sum = sum(sum(row) for row in matrix)
print(total_sum)
# Find maximum and minimum value
max_value = max(max(row) for row in matrix)
print(max_value)
min_value = min(min(row) for row in matrix)
print(min_value)