from RepoDb import RepoDb
from sqlalchemy import text, asc
from Flights import Flights
from Airline_companies import Airline_companies
from Countries import Countries
from Users import Users
from exceptions.company_not_exists_exception import CompanyNotExistsException # to check
from exceptions.Flight_Does_Not_Exist_Exception import FlightDoesNotExistException
from exceptions.AirlineCompanyDoesNotExistException import AirlineCompanyDoesNotExistException
from exceptions.CountriesDoesNotExist import CountriesDoesNotExist
from exceptions.UserDoesNotExistException import UserDoesNotExistException
from db_config import local_session, create_all_entities
from abc import ABC, abstractmethod
from FacadeBase import FacadeBase
# needs to inherit from FacadeBase
repo = RepoDb(local_session)


class AnonymousFacade:
    def __init__(self): # to check
        self.repo = RepoDb(local_session)

    def login(self, username, password):
        error_check = repo.get_by_id(Users, Users.id)
        if error_check is None:
            raise UserDoesNotExistException('there are users!')
        repo.get_by_id(Users.username)
        repo.get_by_id(Users.password)

# might not be necessary to check
#    def password(self, customer):
#        error_check = repo.get_by_id(Users, Users.id)
#        if error_check is None:
#            raise UserDoesNotExistException('there are users!')
#        repo.get_by_id(Users.password)
# might not be necessary to check

    def create_new_user(self, user):
        repo.add(self, Users)

    def add_customer(self, customer):
        pass

