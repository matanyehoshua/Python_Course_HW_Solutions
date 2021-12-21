# name the db flights_db (in the connection string)
# create a class for each table (inherit from Base):
# flights, countries, tickets, airline_companies, users, customers, user_roles, administrators.
# add the constraints to the fields (according to the diagrams)


import sys
from sqlalchemy import asc, text, desc
from Flights import Flights
from Countries import Countries
from Tickets import Tickets
from Airline_companies import Airline_companies
from Users import Users
from Customers import Customers
from User_roles import User_roles
from Administrators import Administrators

class RepoDb:
    def __init__(self, local_session):
        self.local_session = local_session

    def reset_auto_inc(self, table_class):
        self.local_session.execute(f'TRUNCATE TABLE {table_class.__tablename__} RESTART IDENTITY CASCADE')

    def get_by_id(self, table_class, id):
        return self.local_session.query(table_class).get(id)

    def get_all(self, table_class):
        return self.local_session.query(table_class).all()

    def get_all_limit(self, table_class, limit_num):
        return self.local_session.query(table_class).limit(limit_num).all()

    def get_all_order_by(self, table_class, column_name, direction=asc):
        return self.local_session.query(table_class).order_by(direction(column_name)).all()

    def get_by_condition(self, table_class, cond):
        query_result = self.local_session.query(table_class)
        result = cond(query_result)
        return result

    def add(self, one_row):
        self.local_session.add(one_row)
        self.local_session.commit()

    def add_all(self, rows_list):
        self.local_session.add_all(rows_list)
        self.local_session.commit()

    def delete_by_id(self, table_class, id_column_name, id):
        self.local_session.query(table_class).filter(id_column_name == id).delete(synchronize_session=False)
        self.local_session.commit()

    def update_by_id(self, table_class, id_column_name, id, data):
        self.local_session.query(table_class).filter(id_column_name == id).update(data)
        self.local_session.commit()

    def update_by_column_value(self, table_class, column_name, value, data):
        self.local_session.query(table_class).filter(column_name == value).update(data)
        self.local_session.commit()

    def get_by_column_value(self, table_class, column_name, value):
        return self.local_session.query(table_class).filter(column_name == value).all()

    def get_by_ilike(self, table_class, column_name, exp):
        return self.local_session.query(table_class).filter(column_name.ilike(exp)).all()