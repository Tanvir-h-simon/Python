# Sort ascending
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort()
print(this_list)

this_list = [50, 100, 65, 82, 23]
this_list.sort()
print(this_list)

# Sort descending
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort(reverse = True)
print(this_list)

this_list = [100, 50, 65, 82, 23]
this_list.sort(reverse = True)
print(this_list)

# Reverse a list
this_list = [50, 100, 65, 82, 23]
this_list.sort()
this_list.reverse()
print(this_list)

# Case insensitive sort
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort()
print(this_list)

this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort(key = str.lower)
print(this_list)