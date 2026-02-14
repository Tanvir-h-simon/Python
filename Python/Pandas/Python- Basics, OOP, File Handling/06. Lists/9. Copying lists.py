# Copy (Shallow copy) a list
list1 = ["apple", "banana", "cherry"]
list2 = list1.copy() # Returns a shallow copy of the list.
print(list2)

# What is shallow copy? - dependent -> A shallow copy means the outer list is copied, but the inner (nested) objects are not.
a = [1, 2, 3]
b = a.copy()

b[0] = 100
print("a:", a)
print("b:", b)

a = [[1, 2], [3, 4]]
b = a.copy()

b[0][0] = 99 # Both lists changed — because the inner lists are shared (they point to the same memory).
             # That’s the essence of a shallow copy: it copies references, not nested data.
print("a:", a)
print("b:", b)

# Deep copy- independence
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 99
print("a:", a) # Not changed
print("b:", b)

# Make a copy of a list with the list() method
list1 = ["apple", "banana", "cherry"]
list2 = list(list1) 
print(list2)

# Make a copy of a list with the : operator
list1 = ["apple", "banana", "cherry"]
list2 = list1[:] 
print(list2)