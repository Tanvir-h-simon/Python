print(10 > 9)
print(10 == 9)
print(10 < 9)

x = "Hello"
y = 15
print(bool(x)) # Any string is True, except empty strings.
# print(bool(""))
print(bool(y)) # Any number is True, except 0
# print(bool(0))
bool(["apple", "cherry", "banana"]) # Any list, tuple, set, and dictionary are True, except empty ones.
# The following will return False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))