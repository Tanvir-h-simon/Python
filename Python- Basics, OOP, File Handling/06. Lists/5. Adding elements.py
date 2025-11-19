# append()
this_list = ["apple", "banana", "cherry"]
this_list.append("mango") # Adds an element to the end of the list
print(this_list)

# insert(i, x) -> Inserts element x at position i.
this_list.insert(2, "watermelon")
print(this_list) 

# extend(iterable) -> Adds multiple elements from another iterable (list, tuple, etc.) to the end.
list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2) 
print(list1)

this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)