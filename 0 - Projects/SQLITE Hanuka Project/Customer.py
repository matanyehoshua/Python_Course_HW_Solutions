# SQLITE Hanuka Project

# class Customer
class Customer:
    # __init__
    def __init__(self, id, fname, lname, address, mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile = mobile

# __repr__
    def __repr__(self):
        return str(self.__dict__)
# __str__
    def __str__(self):
        return str(self.__dict__)