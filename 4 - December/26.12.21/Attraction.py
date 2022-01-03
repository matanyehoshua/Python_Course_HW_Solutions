# sqlalchemy: create table- attraction: id, name, price (for example: museum, national-park, etc)

from sqlalchemy import Column, BigInteger, String, Integer
from sqlalchemy.orm import relationship, backref
from db_config import Base

# Create table for Attraction:
class Attraction(Base):
    __tablename__ = 'attraction'

    # attraction table:
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(String())
    price = Column(Integer)
    # relationship
    visit_id = relationship("Association", backref=backref("attraction", uselist=True))
    #__repr__:
    def __repr__(self):
        return f'\n<id={self.id} name={self.name} price={self.price} visit_id={self.visit_id}>'
    #__str__:
    def __str__(self):
        return f'<id={self.id} name={self.name} price={self.price} visit_id={self.visit_id}>'