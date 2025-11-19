# A set is a collection which is unordered, unchangeable, and unindexed.
this_set = {"apple", "banana", "cherry"}
print(this_set)
print(type(this_set))
# Set items are unordered, unchangeable, and do NOT allow duplicate values.
# Access items:
# print(this_set[0]) # Error
try:
    print(this_set[0])
except:
    print("Sets are unindexed") # unindexed -> unchangeable
    
for x in this_set:
    print(x)

print("banana" in this_set)  
print("banana" not in this_set)  

this_set = {"apple", "banana", "cherry", "apple"}
print(this_set) # Sets are unordered and do not allow duplicate values 

# True and 1 is considered the same value
this_set = {"apple", "banana", "cherry", True, 1, 2}
print(this_set)

# False and 0 is considered the same value
this_set = {"apple", "banana", "cherry", False, True, 0}
print(this_set)

# Set items can be of any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
mix_set = {"abc", 34, True, 40, "male"}

# Loop through in a set
this_set = {"apple", "banana", "cherry"}
for x in this_set:
    print(x)