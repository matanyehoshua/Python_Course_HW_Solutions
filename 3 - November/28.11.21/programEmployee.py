# importing abstract class and method
from abc import ABC, abstractmethod

### Employee abstract class
class Employee(ABC):
    @abstractmethod
    def __init__(self, id, name, address, age):
        self.id = id
        self.name = name
        self.address = address
        self.age = age

    def calculateSalary(self):
        @abstractmethod
    # here it will calculate the worker or manager's salary
    #    print (f' the x salary is: {x}')
        def __str__(self):
            return f'the worker salary is: '

# compilation error due to class being abstract
# a = Employee(1, 'Nissim', 'Kiryat Moshe 31', 30)
# a.calculateSalary()
# print(a)