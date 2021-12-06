# Car.py
# importing time, and configurations
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db_config import Base

# creating class Car
class Car(Base):
    __tablename__ = 'Cars'
    id = Column(Integer(), primary_key=True)
    model = Column(String(25), nullable=False, unique=True)
    brand = Column(String(80), nullable=False, unique=True, index=True)
    year = Column(DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return f'\n<Car id={self.id} model={self.model} brand={self.brand} year_created={self.year}>'

    def __str__(self):
        return f'<Car id={self.id} model={self.model} brand={self.brand} year_created={self.year}>'

