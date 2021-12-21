# name the db flights_db (in the connection string)
# create a class for each table (inherit from Base):
# flights, countries, tickets, airline_companies, users, customers, user_roles, administrators.
# add the constraints to the fields (according to the diagrams)

from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

# created table for user_roles
class User_roles(Base):
    __tablename__ = 'user_roles'

    # user_roles table
    id = Column(Integer(), primary_key=True, autoincrement=True)
    role_name = Column(String(), unique=True)

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} role_name={self.role_name}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} role_name={self.role_name}>'