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


a = Worker(1, 'Nissim', 'Kiryat Moshe 31', 30, 9, 35)
a.calculateSalary()
print(a)
