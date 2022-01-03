# association table

from sqlalchemy import Column, BigInteger, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base

# Create table for association:
class Association(Base):
    __tablename__ = 'association'

    # association table:
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(String())
    price = Column(Integer)
    attractions_id = Column(BigInteger(),ForeignKey('attraction'))
    visit_id = Column(BigInteger(), ForeignKey('visit'))


    #__repr__:
    def __repr__(self):
        return f'\n<id={self.id} name={self.name} price={self.price} visit_id={self.visit_id}>'
    #__str__:
    def __str__(self):
        return f'<id={self.id} name={self.name} price={self.price} visit_id={self.visit_id}>'