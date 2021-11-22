# Page 25_8

# checks if the number is positive and stores it
x = int(input("enter a number: "))
if x > 0:
    lowest_positive = x

# runs a loop that prints the lowest positive number until a zero or a negative number is entered
while x > 0:
        print (f'the lowest positive number is: {lowest_positive}')
        x = int(input("enter a number: "))
        if x < lowest_positive:
            lowest_positive = x
            if x <= 0:
                break