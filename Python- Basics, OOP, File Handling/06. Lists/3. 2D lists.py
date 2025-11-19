matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

print(matrix)

# Nested iteration
for row in matrix:
    for value in row:
        print(value, end= " ")
    print()    

# Accessing elements
print(matrix[0][1]) # matrix[row][column]
print(matrix[1][2])
matrix[0][1] = 5
print(matrix)
matrix[0][1] = 2

# Accessing with slicing (Rows)
# Slicing rows (outer list):
print(matrix[:2]) # matrix[start:end] -> First two rows
# Slicing columns (inner list):
print(matrix[0][:3]) # First three elements of first row
print(matrix[1][:3]) # First three elements of second row
col1 = [row[0] for row in matrix]
print(col1)
col2 = [row[1] for row in matrix]
print(col2)