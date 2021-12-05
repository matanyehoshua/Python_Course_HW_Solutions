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

# Kablan class
class Kablan(Employee):
    def __init__(self, id, name, address, age, number_of_projects, rate_per_project):
        Employee.__init__(self, id, name, address, age)
        self.number_of_projects = number_of_projects
        self.rate_per_project = rate_per_project
    def calculateSalary(self):
        kablan_salary = self.number_of_projects * self.rate_per_project
        print (f'the kablan salary is: {kablan_salary}')
        return kablan_salary
    def __str__(self):
        return f"the kablan's number of projects is: {self.number_of_projects}\nthe kablan's rate_per_project is: {self.rate_per_project}"


a = Kablan(1, 'Rahamim', 'Rishon', 40, 3, 10000)
a.calculateSalary()
print(a)
