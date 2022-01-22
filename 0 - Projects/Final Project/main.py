# name the db flights_db (in the connection string)
# create a class for each table (inherit from Base):
# flights, countries, tickets, airline_companies, users, customers, user_roles, administrators.
# add the constraints to the fields (according to the diagrams)

import sys
from datetime import datetime
from Flights import Flights
from Countries import Countries
from Tickets import Tickets
from Airline_companies import Airline_companies
from Users import Users
from Customers import Customers
from User_roles import User_roles
from Administrators import Administrators
from RepoDb import RepoDb
from sqlalchemy import asc, text, desc
from db_config import local_session, create_all_entities
from datetime import datetime

# create tables
create_all_entities()

repo = RepoDb(local_session)

repo.reset_auto_inc(Tickets)
repo.reset_auto_inc(Flights)
repo.reset_auto_inc(Administrators)
repo.reset_auto_inc(Airline_companies)
repo.reset_auto_inc(Users)
repo.reset_auto_inc(User_roles)
repo.reset_auto_inc(Countries)
repo.reset_auto_inc(Customers)



repo.add(Countries(id=1, name='Japan'))
repo.add(Countries(id=2, name='Israel'))

repo.add(User_roles(id=1, role_name='admin'))
repo.add(User_roles(id=2, role_name='security'))

repo.add(Users(id=1, username='Rachel', password='1234', email='rachelg@gmail.com', user_role_id=1))
repo.add(Users(id=2, username='Nissim', password='123432', email='nissim@gmail.com', user_role_id=1))

repo.add(Airline_companies(id=1, name='John Airways', country_id=1, user_id=1))

repo.add(Flights(id=1, airline_company_id=1, origin_country_id=1, destination_country_id=1, \
departure_time=datetime(2021, 12, 21, 16, 30, 0), landing_time=datetime(2021, 12, 21, 23, 49, 0), remaining_tickets=2))

repo.add(Flights(id=2, airline_company_id=1, origin_country_id=2, destination_country_id=1, \
departure_time=datetime(2021, 12, 22, 16, 30, 0), landing_time=datetime(2021, 12, 22, 23, 49, 0), remaining_tickets=2))


repo.add(Customers(id=1, first_name='Dor', last_name='Yuval', address='dory@gmail.com', phone_no=42142532, user_id=1))
repo.add(Customers(id=2, first_name='Mor', last_name='Hubal', address='morh@gmail.com', phone_no=44325324, user_id=2))

repo.add(Tickets(id=1, flight_id=1, customer_id=1))
repo.add(Tickets(id=2, flight_id=2, customer_id=2))

repo.add(Administrators(id=1, first_name='Haim', last_name='Ronen', user_id=1))
repo.add(Administrators(id=2, first_name='Shay', last_name='Hen', user_id=2))




flights = repo.get_all(Flights)
print(flights)

countries = repo.get_all_limit(Countries, 3)
print(countries)

flights = repo.get_all_order_by(Airline_companies, Airline_companies.name, asc)
print('asc', flights)

flights = repo.get_all_order_by(Airline_companies, Airline_companies.name, desc)
print('desc', flights)



# nissim = Users(username='nissim', email='nissim@somewhere.com')
# repo.add(nissim)

# users_list = [Users(username='gal', email='gal@gal.com'), Users(username='jibs', email='job@jibs.com')]
# repo.add_all(users_list)

repo.update_by_column_value(Users, Users.username, 'nissim', {Users.username: 'new nissim', 'email':'nissim2@somewhere.com'})

# repo.add(Users(id=1, username='rachel', password=1234, email='rachelg@gmail.com'))

# user1 = Users(id=2, username='tomer23', password=1234, email='tomer23@gmail.com')
# user2 = Users(id=3, username='avi34', password=1234, email='avi34@gmail.com')
# users_ls = [user1, user2]
# repo.add_all(users_ls)

print(repo.get_by_ilike(Users, Users.username, '%nissim%'))
print(repo.get_by_id(Users, 2))
print('> 1', repo.get_by_condition(Users, lambda query: query.filter(Users.id > 1).all()))
print('> 2, first', repo.get_by_condition(Users, lambda query: query.filter(Users.id > 2).first()))
# print('> 3, first', repo.get_by_condition(Users, lambda query: query.filter(Users.id > 3 and Users.id > 4).first()))
