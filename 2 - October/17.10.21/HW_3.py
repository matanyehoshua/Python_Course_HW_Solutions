# HW_3
# create a function that prints the numbers between 1-x. accept the x as parameter. default value should be 10

# prints the numbers from 1 to the entered number
def printer(x = 10):
    n = 1
    for i in range (x):
        print(n)
        n += 1
# user set the printing limit
x = int(input("enter a number: "))
printer(x)
