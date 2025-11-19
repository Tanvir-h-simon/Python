a = 33
b = 200
if b > a:
  print("b is greater than a") # Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
  
# if b > a:
# print("b is greater than a") # error

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
  
# Boolean variables can be used directly in if statements without comparison operators:
is_logged_in = True
if is_logged_in:
  print("Welcome back!")