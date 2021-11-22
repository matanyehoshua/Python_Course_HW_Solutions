# page 26_16

# inputs 2 numbers
x = int(input("enter a number: "))
y = int(input("enter another number: "))
mul = 0

# runs a loop that adds the x number the amount of y is, essentially it is x - y times
for i in range(y):
    mul = mul + x

# prints the result
print (f'the numbers multiplied total is: {mul}')

