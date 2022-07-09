from RepoDb import RepoDb
from sqlalchemy import text, asc
from Flights import Flights
from Airline_companies import Airline_companies
from Countries import Countries
from Users import Users
from Customers import Customers
from exceptions.company_not_exists_exception import CompanyNotExistsException # to check
from exceptions.Flight_Does_Not_Exist_Exception import FlightDoesNotExistException
from exceptions.AirlineCompanyDoesNotExistException import AirlineCompanyDoesNotExistException
from exceptions.CountriesDoesNotExist import CountriesDoesNotExist
from exceptions.UserDoesNotExistException import UserDoesNotExistException
from db_config import local_session, create_all_entities
from abc import ABC, abstractmethod
from FacadeBase import FacadeBase
from LoginToken import LoginToken
from exceptions.PasswordIncorrectException import PasswordIncorrectException
# needs to inherit from FacadeBase
repo = RepoDb(local_session)


class AnonymousFacade(FacadeBase):
    def __init__(self):
        self.repo = RepoDb(local_session)

    def login(self, username, password):
        users_list = repo.get_all(Users)
        user = list(filter(lambda u: u.username == username, users_list))[0]
        if user is None:
            raise UserDoesNotExistException('there are users!')
        if user.password != password:
            raise PasswordIncorrectException('Password is incorrect! Please try again')
        return LoginToken(user.id, user.username, user.user_role_id)


    def create_new_user(self):
        repo.add(Users)

    def add_customer(self):
        repo.add(Customers)

