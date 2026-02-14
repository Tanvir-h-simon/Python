a = 33
b = 200
if b > a:
  pass

'''
The pass statement is useful in several situations:

* When you're creating code structure but haven't implemented the logic yet
* When a statement is required syntactically but no action is needed
* As a placeholder for future code during development
* In empty functions or classes that you plan to implement later
'''
age = 16
if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")
  
# score = 85
# if score > 90:
#   # This is excellent
# # This will raise an IndentationError

# score = 85
# if score > 90:
#   pass # This is excellent
# print("Score processed")

value = 50
if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")