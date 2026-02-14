# A function is a block of code which only runs when it is called.
# A function helps avoiding code repetition.

# Define a function
'''
A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive
'''
def greet():
    print("Hello from a function")
    
# Calling a function
def my_function():
    print("Hello from a function")
    
my_function()
my_function() # We can call the same function multiple times
my_function()

# Return values
def get_greeting():
    return "Hello from a function"

# message = get_greeting()
# print(message)
print(get_greeting())

def my_function(x, y):
    return x + y

result = my_function(5, 3)
print(result)

# The pass statement- Function definitions cannot be empty. If we need to create a function placeholder without any code, use the pass statement.
def my_function():
    pass