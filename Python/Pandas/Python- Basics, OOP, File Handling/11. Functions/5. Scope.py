# A variable is only available from inside the region it is created. This is called scope.

# Local scope: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def func_1():
    x = 10
    print(x + 10)

func_1()
# print(x) # Can't access x

# Global Scope- A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 300
def func_2():
    print(x + 10)

func_2()
print(x)


y = 300
def func_3():
    y = 200
    print(y)

func_3()
print(y)

# Global Keyword- The variable belongs to the global scope
def func_4():
    global x
    x = 300
    
func_4()
print(x)

# Nonlocal keyword- The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
def func_5():
    x = "Jane"
    def func_6():
        nonlocal x
        x = "Hello"
    func_6()
    return x

print(func_5())

''' The LEGB Rule-
Python follows the LEGB rule when looking up variable names, and searches for them in this order:
Local- Inside the current function
Enclosing- Inside enclosing functions (from inner to outer)
Global- At the top level of the module
Built-in- In Python's built-in namespace
''' 
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)