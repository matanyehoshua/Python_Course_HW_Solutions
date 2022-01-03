# sqlalchemy: create table- tourist: id, name, origin_country

from sqlalchemy import Column, BigInteger, String
from db_config import Base


# Create table for Tourist:
class Tourist(Base):
    __tablename__ = 'tourist'

    # tourist table:
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(String())
    origin_country = Column(String())

    #__repr__:
    def __repr__(self):
        return f'\n<id={self.id} name={self.name} origin_country={self.origin_country}>'
    #__str__:
    def __str__(self):
        return f'<id={self.id} name={self.name} origin_country={self.origin_country}>'