a = "Hello, World!"
print(a.upper()) # Upper case

a = "Hello, World!"
print(a.lower()) # Lower case

a = " Hello, World! "
print(a.strip()) # Remove Whitespace (the space before and/or after the actual text)
a = " Hello, World! "
print(a.lstrip()) # Removes leading whitespace
a = " Hello, World! "
print(a.rstrip()) # Removes trailing whitespace


a = "Hello, World!"
print(a.replace("H", "J")) # Rplaces a string with another string

text = "Python is fun"
print(text.split()) # Separate string, and converts into list. No separator given, so it splits wherever there is space.
# list = ["Hello", "World"]
# print(" ".join(list)) # Joins list into string with separator
print(" ".join(text.split()))
text = "apple,banana,cherry"
print(text.split(",")) # The string is split wherever a comma appears.
text = "2025-11-13"
print(text.split("-"))