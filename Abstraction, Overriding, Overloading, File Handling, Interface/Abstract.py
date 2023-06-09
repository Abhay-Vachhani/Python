# # Non abstract
# class Person:
#     def name(self):
#         pass
# person = Person()

# from abc import ABC, abstractmethod

# class Person(ABC):
#     @abstractmethod
#     def name(self):
#         pass

# # person = Person() # Error

# class Employee(Person):
#     def name(self):
#         print('The employee name is ...')

# emp = Employee()
# emp.name()

# Create an abstract method having body and use that code further

# from abc import *
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def name(self):
        print('This is a body of abstract method')
    
    def age(self):
        print(20)

# person = Person() # Error

class Employee(Person):
    def name(self): # Override abstract method 'name' of 'Person' class
        print('The overriden method')
        super().name() # Call the abstract method of 'Person' class

emp = Employee()
emp.name()
emp.age()