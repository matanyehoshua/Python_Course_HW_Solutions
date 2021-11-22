# HW_10

# function that checks if the number is in range and returns the number if so, otherwise checks with another number
def getinRange(min = 10, max = 100):
    x = int(input("Enter a number: "))
    check = 0
    for i in range(max + 1):
        if x >= min:
            pass
            check += 1
        if x <= max:
            pass
            check += 1
        if check == 2:
            return(x)
        else:
            check = 0
            x = int(input("Enter a number: "))

# minimal and maximum values are entered from the user, then gets to a function that checks if the number is in range
# if the number is in range, prints that number
x = int(input("enter a minimal value: "))
y = int(input("enter a maximal value: "))
inrange = getinRange(x, y)
print(f'the number in range is: {inrange}')

