from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base

# created table for users
class Users(Base):
    __tablename__ = 'users'

    # users table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    username = Column(String(), unique=True)
    password = Column(String())
    email = Column(String(), unique=True)
    user_role = Column(Integer(), ForeignKey('user_roles.id'))
    user_id = Column(Integer(), ForeignKey('customers.id'), unique=True, nullable=False)
    # relationships:
    user_roles_id = relationship("User_roles", backref=backref("users", uselist=True))

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} username={self.username} password={self.password} email={self.email} \
user_role={self.user_role} user_id={self.user_id} user_roles_id={self.user_roles_id}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} username={self.username} password={self.password} email={self.email} \
user_role={self.user_role} user_id={self.user_id} user_roles_id={self.user_roles_id}>'