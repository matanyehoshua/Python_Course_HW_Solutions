from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base

# created table for airline_companies
class Airline_companies(Base):
    __tablename__ = 'airline_companies'

    # airline_companies table
    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(String(), unique=True)
    country_id = Column(Integer(), ForeignKey('countries.id'))
    user_id = Column(BigInteger(), ForeignKey('users.id'), unique=True)
    # relationships:
    airline_company_id = relationship("Flights", backref=backref("airline_companies", uselist=True))
    countries_id = relationship("Countries", backref=backref("airline_companies", uselist=True))

    # __repr__
    def __repr__(self):
        return f'\n<id={self.id} name={self.name} country_id={self.country_id} user_id={self.user_id} \
airline_company_id={self.airline_company_id} countries_id={self.countries_id}>'

    # __str__
    def __str__(self):
        return f'<id={self.id} name={self.name} country_id={self.country_id} user_id={self.user_id} \
        airline_company_id={self.airline_company_id} countries_id={self.countries_id}>'