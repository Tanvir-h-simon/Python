# Information can be passed into functions as arguments.
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
print()

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.
def my_function(name): # name is a parameter
    print("Hello", name)
    
my_function("Emil") # "Emil" is an argument

# Multiple parameters
def my_function(first_name, last_name):
  print(first_name + " " + last_name)

my_function("Emil", "Refsnes")
print()

# Default Parameter Values
def my_function(name = "friend"):
    print("Hello", name)

my_function()
my_function("Emil")
my_function("Tobias")
my_function("Linus")
print()