from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base

# created table for administrators
class Administrators(Base):
    __tablename__ = 'administrators'

    # administrators table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name = Column(String())
    last_name = Column(String())
    user_id = Column(BigInteger(), ForeignKey('users.id'), unique=True)

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} user_id={self.user_id}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} first_name={self.first_name} last_name={self.last_name} user_id={self.user_id}>'