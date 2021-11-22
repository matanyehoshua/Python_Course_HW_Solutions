# HW_11

# checks which number is the lowest then returns it
def lowest_number(x = 0, y = 0, z = 0):
    checkx = 0
    checky = 0
    checkz = 0
    if x < y:
        checkx += 1
    if x < z:
        checkx += 1
    if y < x:
        checky += 1
    if y < z:
        checky += 1
    if z < x:
        checkz += 1
    if z < y:
        checkz += 1
    if checkx == 2:
        return(x)
    elif checky == 2:
        return(y)
    else:
        checkz == 2
        return (z)

# inputs 3 user entered numbers and calls the function, then prints the lowest number of all 3 entered numbers
x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
z = int(input("enter the third number: "))
_lowest = lowest_number(x, y, z)
print(f'The lowest number is: {_lowest}')