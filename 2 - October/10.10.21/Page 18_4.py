# Page 18_4

# inputs 2 numbers
x = int(input("enter a number"))
y = int(input("enter a number"))

# checks if the first number and second number can be divided by each other without remainders and prints so
if x % y == 0:
    print ("the first number can be divided by the second number without remainder")
if y % x == 0:
    print ("the second number can be divided by the first number without remainder")