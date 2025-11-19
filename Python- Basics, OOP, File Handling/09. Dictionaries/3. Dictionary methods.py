# Dictionary constructor
this_dict = dict(name = "John", age = 36, country = "Norway")
print(this_dict)

# Dictionary length
print(len(this_dict))

# Copy dictionary
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict2 = dict1.copy()
print(dict2)

# dict()- Make a copy of a dictionary with the dict() function
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict2 = dict(dict1)
print(dict2)