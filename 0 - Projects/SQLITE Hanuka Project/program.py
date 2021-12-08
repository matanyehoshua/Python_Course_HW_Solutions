# SQLITE Hanuka Project
import sqlite3
from Customer import Customer
from CustomerDataAccess import CustomerDataAccess
# setting up the cursor
con = sqlite3.connect('Customer.db')
cursor = con.cursor()

# this will enumerate the columns with the data provided
for row in enumerate(cursor):
    print(row)

# function that adds a customer into the table - UNUSED in the main code but still provided as reference
def add_customer(cursor, table, id, fname, lname, address, mobile):
    cursor.execute(f'INSERT INTO {table} VALUES ({id}, "{fname}", "{lname}", "{address}", {mobile})')

# function that prints all the customers in the table - UNUSED in the main code but still provided as reference
def print_all_customers(cursor):
    cursor.execute("Select * from Customer")

# function that adds a customer into the table - Option 3
def insert_customer (cursor, id, fname, lname, address, mobile):
    cursor.execute(f"DELETE FROM Customer WHERE id = {id}")
    con.commit()
    cursor.execute(f'INSERT INTO Customer (id, fname, lname, address, mobile) \
    VALUES ({id}, "{fname}","{lname}", "{address}", "{mobile}")')
    con.commit()
    con.close()

# function that deletes a customer from the table - Option 4
def delete_customer (cursor, id):
    cursor.execute(f"DELETE FROM Customer WHERE id = {id}")
    con.commit()
    print(f'Customer has been removed from the table')
    con.close()

# function that shows all the customers in the table - Option 1
def get_all_customers (cursor):
    cursor.execute("Select * from Customer")
    _list = [Customer(row[0], row[1], row[2], row[3], row[4]) for row in cursor]
    print(_list)

# function that shows a customer by its ID - Option 2
def get_customers_by_id (cursor, id):
        customer = cursor.execute(f'Select * from Customer where id = {id}').fetchone()
        print(Customer(customer[0], customer[1], customer[2], customer[3], customer[4]))

# function that changes a customer from the table - Option 5
def update_customer(cursor, id, fname, lname, address, mobile):
    cursor.execute(f"DELETE FROM Customer WHERE id = {id}")
    con.commit()
    cursor.execute(f'INSERT INTO Customer (id, fname, lname, address, mobile) \
    VALUES ({id}, "{fname}","{lname}", "{address}", "{mobile}")')
    con.commit()
    con.close()

# Display Menu, user can choose between 1-6 available options, option 6 just exits the program,
# options 3 and 5 overwrite existing data
def main():
    choice = input(f'---Customers Database:---, Please choose an option: 1-6\n\
1. Get all customers\n2. Get customer by id\n3. Insert customer (WARNING: IF SELECTED ID IS USED, THE DATA WILL BE OVERWRITTEN)\
\n4. Delete customer\n5. Update customer (WARNING: IF SELECTED ID IS USED, THE DATA WILL BE OVERWRITTEN)\n6. Exit')
    if choice.isnumeric():
        choice = int(choice)
        if choice == 1:
            get_all_customers(cursor)
        elif choice == 2:
            customer_id = int(input(f'Enter a Customer ID'))
            get_customers_by_id(cursor, customer_id)
        elif choice == 3:
            customer_id = int(input(f'Enter a Customer ID'))
            customer_fname = input(f'Enter a Customer First name')
            customer_lname = input(f'Enter a Customer Last name')
            customer_address = input(f'Enter a Customer Address')
            customer_mobile = input(f'Enter a Customer Mobile Number')
            print(f'ID:{customer_id}, First Name:{customer_fname}, Last Name:{customer_lname},\
 Address:{customer_address}, Mobile Number:{customer_mobile} Entered')
            insert_customer(cursor,customer_id, customer_fname, customer_lname, customer_address, customer_mobile)
        elif choice == 4:
            deleted_customer_id = int(input(f'Please enter a Customer ID'))
            delete_customer(cursor, deleted_customer_id)
        elif choice == 5:
            customer_id = int(input(f'Enter a Customer ID'))
            customer_fname = input(f'Enter a Customer First name')
            customer_lname = input(f'Enter a Customer Last name')
            customer_address = input(f'Enter a Customer Address')
            customer_mobile = input(f'Enter a Customer Mobile Number')
            print(f'ID:{customer_id}, First Name:{customer_fname}, Last Name:{customer_lname},\
 Address:{customer_address}, Mobile Number:{customer_mobile} Entered')
            update_customer(cursor, customer_id, customer_fname, customer_lname, customer_address, customer_mobile)
        else:
            print(f'You have quit the program')
    else:
        print('You have entered an invalid option, please retry')
        main()

# program starts here and calls to main
main()


