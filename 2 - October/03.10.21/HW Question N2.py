# input numbers from the user. print how many numbers above 77 were entered,
# and what is their sum. when zero is receieved the loop will break

_sum = 0
_above_77 = 0

# Checks to see if number entered is above 77 and also sums up the numbers entered
while True:
    x = int(input("Enter a Number: "))
    _sum = _sum + x
    if x > 77:
        _above_77 = _above_77 + 1
    elif x == 0:
        break

# Prints the Sum of numbers entered and the amount of numbers that are above 77 that have been entered
print("The Sum is: ", _sum)
print("The amount of numbers above 77 is: ", _above_77)
