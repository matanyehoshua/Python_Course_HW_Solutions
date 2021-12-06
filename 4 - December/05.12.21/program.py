# HW Solution 5.12.21

# creating a class named Grade
class Grade:

    # static members
    grade_current_index = 1
    sum_grades = 0
# __init__ configuration
    def __init__(self, _student_name, _topic, _grade):
        Grade.grade_current_index += 1
        self._student_name = _student_name
        self._topic = _topic
        self._grade = _grade
        Grade.sum_grades += self._grade
# creating a function that checks if the last entered grade is higher than avg
    def is_grade_higher_than_avg(self):
        return self._grade > (Grade.sum_grades / Grade.grade_current_index)
# static method that returns the avg of all grades entered
    @staticmethod
    def get_average():
        return Grade.sum_grades / Grade.grade_current_index
# static method that returns the current grade index
    @staticmethod
    def get_grade_current_index():
        return Grade.grade_current_index
# a getter that returns the grade
    @property
    def grade(self):
        return self._grade
# a setter that sets the grade if a number has been entered between 0-100 and only integer,
# otherwise returns a message to enter a correct number
    @grade.setter
    def grade(self, new_grade):
        if (new_grade >= 0 and new_grade <= 100) and isinstance(new_grade, int):
            self._grade = new_grade
        else:
            print(f'please enter a valid grade')
# a getter that returns the student name
    @property
    def student_name(self):
        return self._student_name
# a getter that returns the current grade index
    @property
    def grade_index(self):
        return Grade.grade_current_index
# a getter that returns the topic
    @property
    def topic(self):
        return self._topic
# a setter that returns one of the following topics: Math or Python or English
    @topic.setter
    def topic(self, current_topic):
        if current_topic == 'Math' or 'Python' or 'English'
            self._topic = current_topic
        else:
            print(f'please enter a valid topic (Math, Python or English)')

# __str__
    def __str__(self):
        return str(self.__dict__)
# __repr__
    def __repr__(self):
        return str(self.__dict__)