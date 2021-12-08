# SQLITE Hanuka Project
import sqlite3
from Customer import Customer

con = sqlite3.connect('Customer.db')
cursor = con.cursor()

class CustomerDataAccess:
    def __init__(self):
        self.cursor = con.cursor()

    def print_all_customers(cursor):
        cursor.execute("Select * from Customer")

    def insert_customer(cursor, customer):
        cursor.execute(f'INSERT INTO Customer VALUES ({customer.id}, "{customer.fname}", "{customer.lname}", \
         "{customer.address}", {customer.mobile}')

    def delete_customer(cursor, id):
        cursor.execute(f"DELETE FROM Customer WHERE id = {id}")

    def get_all_customers(cursor):
        con.commit()
        cursor.execute("Select * from Customer")
        _list = [Customer(row[0], row[1], row[2], row[3], row[4]) for row in cursor]
        print(_list)
        con.close()

    def update_customer(cursor, id, customer):
        cursor.execute(f'UPDATE Customer SET {customer.id}, "{customer.fname}", \
         "{customer.lname}" "{customer.address}", {customer.mobile} WHERE id = {id}')


    # __repr__
    def __repr__(self):
        return str(self.__dict__)

    # __str__
    def __str__(self):
        return str(self.__dict__)






