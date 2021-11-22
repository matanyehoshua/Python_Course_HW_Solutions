# input a number from the user until a number which is not zero was given.
# input a second number from the user (until a number which is not zero was given).
# if the first number is bigger than the second print “bigger”, and iterate again.
# otherwise, break out of the loop

x = int(input("enter a number: "))
breaker = 0

# Checks if first number is bigger and prints "first number is bigger", otherwise breaks out of the loop
while x != 0 and breaker == 0:
    y = int(input("enter a number: "))
    while y != 0:
        if x > y:
            print( "first number is bigger")
            break
        else:
            breaker = breaker + 1
            break
