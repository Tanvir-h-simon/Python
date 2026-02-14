# Adding an item to the dictionary is done by using a new index key and assigning a value to it
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict["color"] = "red"
print(this_dict)

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.update({"color": "red"})
print(this_dict)