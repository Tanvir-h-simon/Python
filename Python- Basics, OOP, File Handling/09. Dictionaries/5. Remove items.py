# pop()- The pop() method removes the item with the specified key name
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.pop("model")
print(this_dict)

# popitem()- The popitem() method removes the last inserted item
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.popitem()
print(this_dict)

# 'del' keyword - The del keyword removes the item with the specified key name
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del this_dict["model"]
print(this_dict)

# The del keyword can also delete the dictionary completely
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del this_dict
try:
    print(this_dict)
except:
    print("The dictionary is no longer exists.")
    
# clear()- The clear() method empties the dictionary
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.clear()
print(this_dict)