import sys
from Logger import Logger
import logging
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
from FacadeBase import FacadeBase
from AnonymousFacade import AnonymousFacade
from CustomerFacade import CustomerFacade
from AdministratorFacade import AdministratorFacade
from AirlineFacade import AirlineFacade


# create tables - should be used once
create_all_entities()

repo = RepoDb(local_session)
admin = AdministratorFacade()
airline = AirlineFacade
base = FacadeBase()
anonymous = AnonymousFacade()
customer = CustomerFacade()

repo.reset_auto_inc(Tickets)
repo.reset_auto_inc(Flights)
repo.reset_auto_inc(Administrators)
repo.reset_auto_inc(Airline_companies)
repo.reset_auto_inc(Users)
repo.reset_auto_inc(User_roles)
repo.reset_auto_inc(Countries)
repo.reset_auto_inc(Customers)


# testing main starts here:

repo.add(Countries(id=1, name='Japan'))
repo.add(Countries(id=2, name='Israel'))

repo.add(User_roles(id=1, role_name='Administrator'))
repo.add(User_roles(id=2, role_name='Airline Company'))
repo.add(User_roles(id=3, role_name='Customer'))

repo.add(Users(id=1, username='Rachel', password='1234', email='rachelg@gmail.com', user_role_id=1))
repo.add(Users(id=2, username='Nissim', password='123432', email='nissim@gmail.com', user_role_id=1))
repo.add(Users(id=3, username='RON', password='123432', email='RON@gmail.com', user_role_id=2))

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