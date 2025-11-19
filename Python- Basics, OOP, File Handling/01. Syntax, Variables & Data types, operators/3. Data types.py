# """...""" -> Triple-quoted strings
"""
Python has the following data types built-in by default, in these categories:

Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType
"""
# str
x = "Hello World"
print(x)
print(type(x))
# int
x = 5
print(x)
print(type(x))
# float
x = 20.5
print(x)
print(type(x))
# complex
# Complex numbers: a + bj, where a -> real part, b -> imaginary part 
x = 3 + 5j
print(x.real) # 3.0
print(x.imag) # 5.0
print(type(x))
# list
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
# tuple
x = ("apple", "banana", "cherry")
print(x)
print(type(x))
# range
x = range(6)
print(x)
print(type(x))
# dict
x = {"name" : "John", "age" : 36}
print(x)
print(type(x))
# set
x = {"apple", "banana", "cherry"}
print(x)
print(type(x))
# frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
# bool
x = True
print(x)
print(type(x))
# bytes
x = b"Hello"
print(x)
print(type(x))
# bytearray
x = bytearray(5)
print(x)
print(type(x))
# memoryview
x = memoryview(bytes(5))
print(x)
print(type(x))
# NoneType
x = None
print(x)
print(type(x))

x = str("Hello World") # str
x = int(20) # int
x = float(20.5) # float
x = complex(1j) # complex
x = list(("apple", "banana", "cherry")) # list
x = tuple(("apple", "banana", "cherry")) # tuple
x = range(6) # range
x = dict(name="John", age=36) # dict
x = set(("apple", "banana", "cherry")) # set
x = frozenset(("apple", "banana", "cherry")) # frozenset
x = bool(5) # bool
x = bytes(5) # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview