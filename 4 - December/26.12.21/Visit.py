# sqlalchemy: create table- visit: id, tourist_id, attraction_id, year_of_visit [many-to-many]

from sqlalchemy import Column, BigInteger, String, Integer
from sqlalchemy.orm import relationship, backref
from db_config import Base

# create table Visit:
class Visit(Base):
    __tablename__ = 'visit'

    # visit table:
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    tourist_id = Column(Integer())
    attraction_id = Column(Integer())
    year_of_visit = Column(Integer())
    # relationship
    attractions_id = relationship("Association", backref=backref("visit", uselist=True))

    #__repr__:
    def __repr__(self):
        return f'\n<id={self.id} tourist_id={self.tourist_id} attraction_id={self.attraction_id} \
year_of_visit={self.year_of_visit}>'
    #__str__:
    def __str__(self):
        return f'<id={self.id} tourist_id={self.tourist_id} attraction_id={self.attraction_id} \
year_of_visit={self.year_of_visit}>'