import random

x = random.random() # Random float between 0 and 1
print(x)

x = random.uniform(10, 20) # Random float in a range
print(x)

x = random.randint(1, 6) # Random integer (inclusive)
print(x)

x = random.randrange(1, 10, 2) # Random integer with step
print(x)

items = (["apple", "banana", "cherry"]) # Random choice from a list
print(random.choice(items))

# Import a specific funtion
from random import randint
print(randint(1, 6))