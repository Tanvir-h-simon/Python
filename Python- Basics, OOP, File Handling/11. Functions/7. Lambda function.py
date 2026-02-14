# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax- lambda arguments : expression

# Without lambda function:
def squared_number(num):
    return num * num

print(squared_number(5))
print(squared_number(10))

# lambda function:
squared_number = lambda num: num * num # lambda arguments : expression
print(squared_number(5))
print(squared_number(10))

# Without lambda function:
def multiply(a, b):
    return a * b

print(multiply(5, 10))

# lambda function:
multiply = lambda a, b: a * b
print(multiply(5, 10))