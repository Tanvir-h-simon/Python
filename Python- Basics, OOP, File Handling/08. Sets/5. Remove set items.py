# remove()- If the item to remove does not exist, remove() will raise an error.
this_set = {"apple", "banana", "cherry"}
this_set.remove("banana")
try:
    this_set.remove("mango")
except:
    print("THe item is not in the set")    
print(this_set)

# discard()- If the item to remove does not exist, discard() will NOT raise an error.
this_set = {"apple", "banana", "cherry"}
this_set.discard("banana")
this_set.discard("mango")
print(this_set)

# pop()- The pop() method will remove a random item. Sets are unordered, so when using the pop() method, we do not know which item that gets removed.
this_set = {"apple", "banana", "cherry"}
x = this_set.pop()
print(x)
print(this_set)

# clear()- The clear() method empties the set
this_set = {"apple", "banana", "cherry"}
this_set.clear()
print(this_set)

# clear()- The del keyword will delete the set completely
this_set = {"apple", "banana", "cherry"}
del this_set
try:
    print(this_set)
except:
    print("The set is already deleted.")