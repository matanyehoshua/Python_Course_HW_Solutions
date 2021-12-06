# main.py

from Car import Car
from db_config import local_session, create_all_entities

# create tables
create_all_entities()

# add a list of cars to the table
cars_list = [Car(id=1, model='Aventador', brand='Lamborghini', year=2022), Car(id=2, model='Chiron', brand='Bugatti', year=2022)]
local_session.add_all(cars_list)
local_session.commit()

# print all cars from the table
cars = local_session.query(Car).all()
print(cars)