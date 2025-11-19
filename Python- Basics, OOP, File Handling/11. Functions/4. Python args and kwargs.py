# By default, a function must be called with the correct number of arguments.
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args:
# The *args parameter allows a function to accept any number of positional arguments.
def num_func(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(num_func(5, 6))
print(num_func(1, 2, 3))
print(num_func(10, 20, 30, 40))

def num_set(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(num_set(3, 7, 2, 9, 1))

def student(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

student("Emil", "Tobias", "Linus") # Tuples

# Arbitrary Keyword Arguments - **kwargs:
# The **kwargs parameter allows a function to accept any number of keyword arguments.
def student(**kwargs):
    print("Type:", type(kwargs))
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])
    print("All data:", kwargs)

student(name = "Tobias", age = 30, city = "Bergen")

def func(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

func("Tanvir", age = 25, city = "Kuala Lumpur", hobby = "coding")

# Combining *args and **kwargs
def func(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

func("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Unpacking arguments
# Unpacking Lists with *:
def sum(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = sum(*numbers)
print(result)

# Unpacking Dictionaries with **:
def name(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
name(**person)
