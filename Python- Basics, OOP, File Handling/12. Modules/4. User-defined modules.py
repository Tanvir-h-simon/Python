import math_tools

print(math_tools.add(5, 3))
print(math_tools.subtract(5, 3))
print(math_tools.pi)

# Import specific functions
from math_tools import add
print(add(10, 4))

from math_tools import subtract
print(subtract(10, 4))


# Rename the module
import math_tools as mt

print(mt.add(9, 2))
print(mt.subtract(10, 5))

'''
Where Python looks for your module ?
When you do import module, Python searches:
1. The current working directory
2. Installed packages
3. Paths listed in sys.path
import sys
print(sys.path)
'''