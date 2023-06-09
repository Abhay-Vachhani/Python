from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def name(self, nm):
        print('Person Name is', nm)
    
    @abstractmethod
    def age(self):
        print('Person Age')

# person = Person() # Error

class Employee(Person):
    def name(self, nm):
        print('Employee Name is ', nm)
        super().name(nm)
    
    def age(self):
        print('Employee Age')
        super().age()
    
emp = Employee()
emp.name('Dev')
emp.age()