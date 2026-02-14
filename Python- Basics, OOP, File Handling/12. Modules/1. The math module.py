import math # Built-in module

x = math.pow(2, 2)
print(x)

x = math.sqrt(64)
print(x)

x = math.ceil(1.4)
print(x)

x = math.floor(1.4)
print(x)

x = math.pi
print(x)

# Import a specific funtion
from math import pow
print(pow(2, 2))

# Import a specific funtion
from math import sqrt
print(sqrt(4))

# Import all function
from math import * # Not recommended
print(pow(2, 2)) 

# Build-in function:
x = min(5, 10, 25)
print(x)

y = max(5, 10, 25)
print(y)

x = abs(-7.25)
print(x)

x = pow(4, 3)
print(x)