from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base

# created table for user_roles
class User_roles(Base):
    __tablename__ = 'user_roles'

    # user_roles table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    role_name = Column(String(), unique=True)
    # relationships:
    users_id = relationship("Users", backref=backref("user_roles", uselist=True))

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} role_name={self.role_name} users_id={self.users_id}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} role_name={self.role_name} users_id={self.users_id}>'