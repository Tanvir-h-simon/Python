class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Tanvir", 24)
p2 = Person("Israt", 22)

print(p1.name, p1.age)
print(p2.name, p2.age)

'''
Why use __init__?
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
__init__() initializes object attributes.
The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

'''
# Without using __init__:
class Person:
  pass

# p1 = Person("Tanvir", 24) # Error
p1.name = "Tanvir"
p1.age = 25
print(p1.name, p1.age)

# With using __init__:
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name, p1.age, p1.city, p1.country)

'''
Why use self?
The self parameter is a reference to the current instance of the class. It is used to access properties and methods that belong to the class.
self is required because Python does not automatically know which object’s data we want to access.
- When we create an object, it has its own copy of attributes.
- Inside a method, self tells Python use the attributes of this specific object.
* The self parameter must be the first parameter of any method in the class.
* self Does Not Have to Be Named 'self'
'''
# Accessing Properties with 'self':
class Car:
    def __init__(this, brand, model, year):
        this.brand = brand
        this.model = model
        this.year = year

    def display_info(this):
        print(f"{this.year} {this.brand} {this.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

# Calling Methods with self:
# It is strongly recommended to use self as it is the convention in Python
class Person:
    def __init__(self, name): 
        self.name = name
    
    def greet(self): # Class Methods- All methods must have self as the first parameter.
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")

p1 = Person("Tanvir")
p1.welcome()

# Modify class properties:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self): # Class method
        print("Hello!")

p1 = Person("Tanvir", 24)
print(p1.age)

p1.age = 25
print(p1.age)

del Person.greet # Delete method

del p1.age # Delete property
# print(p1.age) # This would cause an error
print(p1.name)

# Class Properties vs Object Properties:
class Person:
    species = "Human" # Class property

    def __init__(self, name): # # Class Methods
        self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

Person.lastname = "Refsnes" # Modifying Class Properties
p1.city = "Oslo" # Add a new property to an object

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
print(p1.city)

# The __str__ method- a special method that controls how object is displayed as a string.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(Name = {self.name}, Age = {self.age})"

s = Student("Tanvir", 24)
print(s)