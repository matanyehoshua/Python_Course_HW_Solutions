from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

# created table for customers
class Customers(Base):
    __tablename__ = 'customers'

    # customers table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name = Column(String())
    last_name = Column(String())
    address = Column(String())
    phone_no = Column(String(), unique=True)
    user_id = Column(BigInteger(), ForeignKey('users.id'), unique=True)
    customer_id = Column(BigInteger, ForeignKey('flightscustomers.id'), unique=False, nullable=False)

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} address={self.address} \
phone_no={self.phone_no} user_id={self.user_id} customer_id={self.customer_id}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} first_name={self.first_name} last_name={self.last_name} address={self.address} \
phone_no={self.phone_no} user_id={self.user_id} customer_id={self.customer_id}>'