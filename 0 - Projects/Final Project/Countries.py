from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base

# created table for countries
class Countries(Base):
    __tablename__ = 'countries'

    # countries table
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(), unique=True)
    # relationships:
    country_id = relationship("Airline_companies", backref=backref("countries", uselist=True))
    origin_country_id = relationship("Flights", backref=backref("countries", uselist=True))

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} name={self.name} country_id={self.country_id} origin_country_id={self.origin_country_id}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} name={self.name} country_id={self.country_id} origin_country_id={self.origin_country_id}>'