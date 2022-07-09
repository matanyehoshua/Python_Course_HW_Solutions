import pytest
from RepoDb import RepoDb
from AnonymousFacade import AnonymousFacade
from FacadeBase import FacadeBase
from db_config import local_session

repo = RepoDb(local_session)
expected_number_of_flights = 2

def test_login():
    token = AnonymousFacade().login('Rachel', '1234')
    assert token.name == 'Rachel'

def test_get_all_flights():
    flights = FacadeBase().get_all_flights()
    assert len(flights) == expected_number_of_flights
