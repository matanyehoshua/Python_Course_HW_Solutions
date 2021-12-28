# create a table called kita and table called students and make a 1-to-many relationship:
# kita table: id [pk, auto-increment], floor [integer], num_of_students [integer], class_avg [real]. students table: id [pk, auto-increment],
# fname, lname [fname+lname unique], grade_avg [real], kita_id, kitot = relationship(“Kita”, backref=backref(“students”, uselist=True))
# create 2 kitot
# create few students and place them in these kitot
# print the list of students for each kita

from db_config import local_session, create_all_entities
from DbRepo import DbRepo
from Kita import Kita
from Students import Students


repo = DbRepo(local_session)

# checks if the tables do exist, if so it will DROP these tables
local_session.execute('drop TABLE if exists kita cascade')
local_session.commit();
local_session.execute('drop TABLE if exists students cascade')
local_session.commit();

create_all_entities()

# creates 2 instances of Kita
kita1 = Kita(id=1, floor=1, num_of_students=15, class_avg=78)
repo.add(kita1)
kita2 = Kita(id=2, floor=1, num_of_students=20, class_avg=95)
repo.add(kita2)

# creates 2 instanced of Students
student1 = Students(id=1, fname='Nissim', lname='David', grade_avg=77, kita_id=1)
repo.add(student1)
student2 = Students(id=2, fname='Tal', lname='Yoni', grade_avg=76, kita_id=2)
repo.add(student2)

# prints all the students from the Kita and prints the Students list from the Kita
list1 = repo.get_all(Kita)
list2 = repo.get_by_id(Kita, 1)
list3 = repo.get_by_id(Kita, 2)
print(list1)
print(list2)
print(list3)




