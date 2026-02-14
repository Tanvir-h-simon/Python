s = "apple banana apple"

# find(substring) -> returns first index, -1 if not found
print(s.find("apple")) 
print(s.find("orange"))

# index(substring) -> raises ValueError if not found
print(s.index("banana")) 
# print(s.index("orange")) # ValueError

# count(substring) -> counts occurrences of substring
print(s.count("apple"))
print(s.count("a")) 

# startswith(prefix) -> checks if string starts with substring
print(s.startswith("apple"))    
print(s.startswith("banana"))  

# endswith(suffix) -> checks if string ends with substring
print(s.endswith("apple"))   
print(s.endswith("banana"))