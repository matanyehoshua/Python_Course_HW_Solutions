# HW_Solution 17.11.21
import shelve

# UML Implementation
class Grade:
    def __init__(self, id=0, subject_name=None, student_id=0, grade=0):
        self.id = id
        self.subject_name = subject_name
        self.student_id = student_id
        self.grade = grade

    def __str__(self):
        return f'id is: {self.id}, ' f'subject_name is: {self.subject_name}, ' \
                f'student id is: {self.student_id}, ' f'grade is: {self.grade}'

    def __repr__(self):
        return f'id is: {self.id}, ' f'subject_name is: {self.subject_name}, ' \
                f'student id is: {self.student_id}, ' f'grade is: {self.grade}'

    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.grade == other.grade
        elif type(other) in [int, float]:
            return self.id == other
        else:
            # throw error
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Grade):
            return self.grade > other.grade
        elif type(other) in [int, float]:
            return self.id > other
        else:
            # throw error
            return False

    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.grade < other.grade
        elif type(other) in [int, float]:
            return self.id < other
        else:
            # throw error
            return False

    def __add__(self, other):
        self.grade += other
        return self

    def __sub__(self, other):
        self.grade -= other
        return self

# etgar question, that will only work when there is a value stored in the shelve, otherwise it will give an error!
studnet_id = input("please enter a student id ID for grade: ") #etgar, lines 57 - 60 will only work when there is a shelve saved!!!
sh = shelve.open('student_grades.db') # etgar
key = sh[studnet_id] # etgar
print(dict(list(key.items())[3:])) # etgar
# end of etgar part
# creates 4 grades. saves them using shelve lib, uses the id as the key
g1 = Grade(1, 'student1', 1, 20)
g2 = Grade(2, 'student2', 2, 50)
g3 = Grade(3, 'student3', 3, 70)
g4 = Grade(4, 'student4', 4, 100)
sh[str(g1.id)] = g1.__dict__
sh[str(g2.id)] = g2.__dict__
sh[str(g3.id)] = g3.__dict__
sh[str(g4.id)] = g4.__dict__
id = input('please enter student id: ')
if id in sh.keys():
    g = Grade()
    g.__dict__ = sh[id]
    print(g)
sh.close()

