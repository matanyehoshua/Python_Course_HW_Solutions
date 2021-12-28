# like we did in class-
# create a function called invokeme which gets a list argument a function argument func1 and a second function argument func2.
# inside invokeme execute the function on all of the list members and prints the result.
# but this time if the list member is in zugi invoke func1 on the item and if the member is e-zugi invoke fun2 on the item.
# now call this function using 2 lambda expressions and send it a list of numbers

# function that gets a list and two functions, then combines all the items from the list with the two functions
# if the numbers are even the function returns a lambda which increases the item by two,
# if the numbers are odd the function returns a lambda which decreases the item by two.
def invokeme(list1, func1, func2):
    for i in range(len(list1)):
        if list1[i] % 2 != 0:
            list1[i] = func1(list1[i])
        else:
            list1[i] = func2(list1[i])

# calls the function invokeme and sends two lambda expressions, one which increases the item by two
# and one which decreases the item by two
list1 =[5, 6, 7]
invokeme(list1, lambda x: x + 2, lambda x: x - 2)
print(list1)

