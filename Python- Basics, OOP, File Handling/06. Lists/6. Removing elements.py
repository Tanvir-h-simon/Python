# remove() -> Removes first occurrence of x. Raises error if not found.
this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list)
this_list = ["apple", "banana", "cherry", "banana", "kiwi"]
this_list.remove("banana")
print(this_list)
# this_list.remove("mango") # ValueError
# Avoiding error with try–except
try:
    this_list.remove("mango")
except:
    print("Item not found")    

# pop(i) -> Removes and returns the element at index i. If no index, removes last element.
this_list.pop(1)
print(this_list)
this_list.pop()
print(this_list)

# 'del' keyword
this_list = ["apple", "banana", "cherry"]
del this_list[0]
print(this_list)
del this_list # The del keyword can delete the list completely.
# print(this_list) # Error

# clear() -> Removes all elements (empties the list). The list still remains, but it has no content.
this_list = ["apple", "banana", "cherry"]
this_list.clear()
print(this_list)
print(len(this_list))