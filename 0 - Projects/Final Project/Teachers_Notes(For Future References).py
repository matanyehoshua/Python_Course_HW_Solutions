# whenever you insert a FK you must have a corresponding record in the other table
# with this id ... for example if you choose  airline_company_id=1 -> you need to have an airline with PK = 1
# do you understand?
# yes I have made the id... random so errors are from this haha
# if you are using random numbers then you may consider using a get (Select) command
# to retrieve a record and then fetch the id from the record ...
# or get all the records into a list and select a random item and then
# use the PK of the random item you selected ...

# we just need to add CASCADE at the end of the query