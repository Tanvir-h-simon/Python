# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child class
class Student(Person):
    def __init__(self, name, age, student_id, department):
        # Person.__init__(self, name, age)
        super().__init__(name, age) # Call parent constructor
        self.student_id = student_id
        self.department = department

    def show_student(self):
        print(f"ID: {self.student_id}, Department: {self.department}")

p = Person("John", 30)
s = Student("Tanvir", 21, "23121478", "Artificial Intelligence")

p.show_info() # From Person
s.show_info() # From Student    
s.show_student()