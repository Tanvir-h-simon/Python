'''
There are several ways to join two or more sets in Python.
1. The union() and update() methods joins all items from both sets.
2. The intersection() method keeps ONLY the duplicates.
3. The difference() method keeps the items from the first set that are not in the other set(s).
4. The symmetric_difference() method keeps all items EXCEPT the duplicates.

'''
# Union:
# union()- The union() method returns a new set with all items from both sets.
# We can use the | operator instead of the union() method, and we will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# set3 = set1.union(set2)
set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
# set5 = set1.union(set2, set3, set4)
set5 = set1 | set2 | set3 |set4
print(set5)

# Join a set and tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
# z = x | y # Error- The | operator only allows us to join sets with sets, and not with other data types like we can with the union() method.
print(z)

# update()- The update() method inserts all items from one set into another. The update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) # Both union() and update() will exclude any duplicate items.
print(set1)

# Intersection:
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# The & operator only allows us to join sets with sets, and not with other data types like we can with the intersection() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
set3 = set1 & set2
print(set3)

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# Difference:
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
set3 = set1 - set2
print(set3)

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# We can use the ^ operator instead of the symmetric_difference() method, and we will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
set3 = set1 ^ set2
print(set3)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

# Disjoint set- Returns whether two frozensets have an intersection
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
print(set1.isdisjoint(set2))

# Subset- Returns True if this frozenset is a (proper) subset of another
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
print(set1.issubset(set2))

# Superset- Returns True if this frozenset is a (proper) superset of another
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
print(set1.issuperset(set2))