# Keyword arguments(kwargs)- We can send arguments with the key = value syntax:
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

greet(name="Alice", age=25)  # Explicitly specify which is which
greet(age=25, name="Alice")  # Order doesn't matter

# Positional arguments- arguments that are matched to parameters based on their position or order
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

greet("Alice", 25)  # "Alice" goes to name, 25 goes to age
greet(25, "Alice")  # This would be wrong - age comes before name. The order matters

# Mixing Positional and Keyword Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")
    
greet("Alice", age=25)
# greet(name="Alice", 25)  # SyntaxError- positional arguments must come before keyword arguments

# Position-only arguments- To specify positional-only arguments, add , / after the arguments. Everything before the / is positional-only.
def greet(name, age, /):
    print(f"Hello {name}, you are {age} years old")

greet("Alice", 25) # positional arguments
# greet(name="Alice", age=25) #TypeError - cannot use keyword arguments

# Keyword-only arguments- To specify that a function can have only keyword arguments, add *, before the arguments
def greet(name, age, *, country, premium):
    print(f"{name}, {age}, {country}, Premium: {premium}")

greet("Alice", 25, country = "USA", premium = True) # keywords for country and premium
greet("Alice", 25, "USA", True) # TypeError - cannot pass positionally

# Combining Positional-only and Keyword-only arguments
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
# result = my_function(a = 10, b = 5, c = 15, d = 20) # Error
# result = my_function(5, 10, 15, 20) # Error
# Syntax: (positional-only, /, flexible, *, keyword-only)
print(result)