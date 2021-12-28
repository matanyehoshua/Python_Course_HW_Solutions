# Students.py
# students table: id [pk, auto-increment], fname, lname [fname+lname unique], grade_avg [real], kita_id,
# kitot = relationship(“Kita”, backref=backref(“students”, uselist=True))

from sqlalchemy import Column, BigInteger,Integer, String, DateTime, REAL, Date, ForeignKey, UniqueConstraint
from db_config import Base
from sqlalchemy.orm import relationship, backref

class Students(Base):
    __tablename__ = 'students'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    fname = Column(String, unique=True)
    lname = Column(String, unique=True)
    grade_avg = Column(REAL)
    kita_id = Column(Integer)

kitot = relationship('kita', backref=backref('students', uselist=True))

def __str__(self):
    return f'<Students> id:{self.id} fname:{self.fname} lname:{self.lname} grade_avg:{self.grade_avg} \
kita_id:{self.kita_id}'

def __repr__(self):
    return f'<Students> id:{self.id} fname:{self.fname} lname:{self.lname} grade_avg:{self.grade_avg} \
kita_id:{self.kita_id}'
