# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict)
print(type(this_dict))

# Access items- We can access the items of a dictionary by referring to its key name, inside square brackets
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict["brand"])
print(this_dict["model"])
print(this_dict["year"])

# get()- Get values and keys
print(this_dict.get("brand"))
print(this_dict.get("model"))
print(this_dict.get("year"))

print(this_dict.keys())

# Changeable
this_dict["brand"] = "BMW"
print(this_dict.get("brand"))
this_dict.update({"year" : 2020}) # The update() method will update the dictionary with the items from the given argument.
print(this_dict.get("year"))

# Duplicate not allows
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(this_dict)

# The values in dictionary items can be of any data type
this_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(this_dict)

# Check if Key Exists:
if "brand" in this_dict:
    print("Yes, 'model' is one of the keys in the dictionary")
    
# Loop Through a Dictionary:
for x in this_dict:
    print(x) # print all key names one by one

for x in this_dict:
    print(this_dict[x]) # Print all values in the dictionary, one by one
    
# values()- We can also use the values() method to return values of a dictionary
for x in this_dict.values():
    print(x)
    
# keys()- We can use the keys() method to return the keys of a dictionary
for x in this_dict.keys():
    print(x)
    
# items()- Loop through both keys and values, by using the items() method
for x, y in this_dict.items():
    print(x, y)