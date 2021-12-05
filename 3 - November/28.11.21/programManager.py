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

# worker class
class Manager(Employee):
    def __init__(self, id, name, address, age, number_of_employees, employee_rate):
        Employee.__init__(self, id, name, address, age)
        self.number_of_employees = number_of_employees
        self.employee_rate = employee_rate
    def calculateSalary(self):
        manager_salary = self.number_of_employees * self.employee_rate
        print(f'the manager salary is: {manager_salary}')
        return manager_salary
    def __str__(self):
        return f"the manager's number of employees is: {self.number_of_employees}\nthe manager's employee rate is: {self.employee_rate}"


a = Manager(1, 'David', 'Tel Aviv 24', 35, 9, 5000)
a.calculateSalary()
print(a)