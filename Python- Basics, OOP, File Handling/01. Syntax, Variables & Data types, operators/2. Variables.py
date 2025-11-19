a = 10
# y = 'Tanvir'
b = "Tanvir"
print(a)
print(type(a))
print(b)
print(type(b))

# If we want to specify the data type of a variable, this can be done with casting.
a = str(3) # x will be '3'
print(a)
b = int(3) # y will be 3
print(b)
c = float(3) # z will be 3.0
print(c)

# print(a + b) # TypeError
print(b + c)
print(type(b + c))
x = "Python "
y = "is "
z = "awesome"
print(x + y + z) # Concatening

a = 4
A = "Sally"
print(a, A) # A will not overwrite a- python is case-sensitive

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Multi Words Variable Names:
# Camel Case:
myVariableName = "John"
# Pascal Case:
MyVariableName = "John"
# Snake Case: # Most commonly used in Python
my_variable_name = "John"

# Assign values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print(x, y, z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection (list, tuple)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)