# Once a set is created, you cannot change its items, but you can add new items.
this_set = {"apple", "banana", "cherry"}
this_set.add("orange")
print(this_set)

# To add items from another set into the current set
set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "mango", "papaya"}
set1.update(set2)
print(set1)

this_set = {"apple", "banana", "cherry"}
this_list = ["kiwi", "orange"]
this_set.update(this_list)
print(this_set)