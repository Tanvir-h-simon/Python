# Decorators let us add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

# Basic decorator syntax:
'''
@decorator_name
def function_name():
    pass
'''
# Original function:
def greet_func():
    print("Hello")
greet_func()

# Decorator function:
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet_func():
    print("Hello, World!")
greet_func()


# Decorator that accepts no arguments:
# Secure the function with *args and **kwargs arguments
def decorator(func):
    def wrapper(*args, **kwargs):
        # Extra behavior
        return func(*args, **kwargs)
    return wrapper

@decorator
def my_function():
    pass

# Decorator for functions with parameters:
def debug(func):
    def wrapper(*args, **kwargs):
        print("Args:", args)
        print("Kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(5, 3))

# Decorator that accepts arguments:
def decorator_with_args(x, y):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            # Use x, y 
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator

@decorator_with_args(10, 20)
def my_function():
    pass

# Decorator that accepts arguments:
def decorator_with_args(x, y):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator args: x = {x}, y = {y}")
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator

@decorator_with_args(10, 20)
def my_function():
    return 10 + 20
print(my_function())

# Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
def this_function():
    return "Have a great day!"

print(this_function.__name__)