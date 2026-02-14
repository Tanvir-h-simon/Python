# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
# In Python, we are also allowed to extract the values back into variables. This is called "unpacking"
fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
green, yellow, red = fruits
print(green)
print(yellow)
print(red)
print()

number = (10, 20, 30)
a, b, c = number
print(a) 
print(b) 
print(c)
print()

name, age, country = ("Tanvir", 24, "Malaysia")
print(name)
print(age)
print(country)
print()

# The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
green, yellow, *red = fruits # Star Operator (*)
print(green)
print(yellow)
print(red)
print()

number = (1, 2, 3, 4, 5)
a, b, *rest = number
print(a)
print(b)
print(rest)
print()

*first, last = number
print(first)
print(last)
print()

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
green, *tropic, red = fruits
print(green)
print(tropic)
print(red)
print()

# Unpacking in a loop
pairs = [(1, "A"), (2, "B"), (3, "C")]

for num, letter in pairs:
    print(num, letter)