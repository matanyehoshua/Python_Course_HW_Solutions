# main code
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
class Worker(Employee):
    def __init__(self, id, name, address, age, hours_per_day, hour_rate):
        Employee.__init__(self, id, name, address, age)
        self.hours_per_day = hours_per_day
        self.hour_rate = hour_rate
    def calculateSalary(self):
        worker_salary = self.hours_per_day * self.hour_rate
        print (f'the worker salary is: {worker_salary}')
        return worker_salary
    def __str__(self):
        return f"the worker's hours per day is: {self.hours_per_day}\nthe worker's hour rate day is: {self.hour_rate}"

# manager class
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

# kablan class
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



