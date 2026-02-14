# List constructor
# list(iterable): Converts an iterable to list.
print(list("abc"))
# word = list("abc")
# print(word)
word = list(("abc", "Hello")) # Double round brackets: Convert tuple to list
print(word)
fruits = list(("apple", "banana", "cherry")) 
print(fruits)

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# List length
print(len(fruits))

# List sum
number = [1, 2, 3, 4, 5]
print(sum(number))

# List maximum
print(max(number))

# List minimum
print(min(number))

# 2D lists:
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
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