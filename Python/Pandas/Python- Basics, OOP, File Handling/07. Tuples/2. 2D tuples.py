matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Accessing elements
print(matrix[0][1])  # (first row, second column)

# Slicing rows
print(matrix[:2])

# Slicing columns
print(tuple(row[:2] for row in matrix))  # ((1, 2), (4, 5), (7, 8))