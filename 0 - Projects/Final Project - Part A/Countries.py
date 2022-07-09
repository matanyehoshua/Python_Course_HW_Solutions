from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base

# created table for countries
class Countries(Base):
    __tablename__ = 'countries'

    # countries table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(String(), unique=True)

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} name={self.name}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} name={self.name}>'