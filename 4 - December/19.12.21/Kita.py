# Kita.py
# create a table called kita and table called students and make a 1-to-many relationship:
# kita table: id [pk, auto-increment], floor [integer], num_of_students [integer], class_avg [real].

from sqlalchemy import Column, BigInteger,Integer, String, DateTime, REAL, Date, ForeignKey, UniqueConstraint
from db_config import Base
from sqlalchemy.orm import relationship, backref

class Kita(Base):
    __tablename__ = 'kita'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    floor = Column(Integer)
    num_of_students = Column(Integer)
    class_avg = Column(REAL)

# students = relationship("Students", backref=backref("kita", uselist=True))


def __str__(self):
    return f'<Kita> id:{self.id} floor:{self.floor} num_of_students:{self.num_of_students} class_avg:{self.class_avg}'

def __repr__(self):
    return f'<Kita> id:{self.id} floor:{self.floor} num_of_students:{self.num_of_students} class_avg:{self.class_avg}'
