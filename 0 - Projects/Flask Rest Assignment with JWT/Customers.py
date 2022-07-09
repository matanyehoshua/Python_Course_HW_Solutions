import json
from sqlalchemy import BigInteger, String, Column
from db_config import Base

# created table for customers
class Customers(Base):
    __tablename__ = 'customers'

    # customers table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(String())
    address = Column(String())

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} name={self.name} address={self.address}'

    # __str__
    def __str__(self):
        return f'<id={self.id} name={self.name} address={self.address}'

    def toObject(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }