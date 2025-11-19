# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Create an array containing car names
cars = ["Ford", "Volvo", "BMW"]
print(cars)

# Access the Elements of an Array
print(cars[0])
cars[0] = "Toyota"
print(cars)

# The Length of an Array
print(len(cars))

# Looping array elements
for i in cars:
    print(i, end=" ")
print()    
    
# Adding Array Elements
cars.append("Honda")
print(cars)

# Removing Array Elements
cars.pop(1)
try:
    cars.remove("Volvo")
except:
    print("Element is not found in the array")
print(cars)