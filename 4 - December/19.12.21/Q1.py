# like we did in class- create a function called invokeme which gets a list argument and a function argument.
# inside invokeme execute the function on all of the list members and prints the result.
# now call this function using lambda expression and send it a list of numbers. will it work on a tuple? try

# function that takes a list and combines the items in that list with the items from the function
def invokeme(list1, _function):
    for i in range(len(list1)):
        list1[i] = _function(list1[i])

# calls the function invokeme and sends a lambda expression
list1 =[5, 6, 7]
# list1 = (2, 3) - tuple assignment is not supported (tuples are unchangeable) so we cannot use it for lambda
invokeme(list1, lambda x: x + 2)
print(list1)