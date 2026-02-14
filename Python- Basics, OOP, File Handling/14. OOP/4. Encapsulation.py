# In Python, we can make properties private by using a double underscore __ prefix
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private property
    
    def get_age(self):
        return self.__age

p1 = Person("Emil", 25)
print(p1.name)
# print(p1.__age) # This will cause an error
print(p1.get_age())

# Private method:
# Just like private properties with double underscores, private methods cannot be called directly from outside the class. The __validate method can only be used by other methods inside the class.
class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error 