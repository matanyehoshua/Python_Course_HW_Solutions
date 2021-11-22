# HW_8

# function for calculating hekef:
def calchekef(x):
    p = 2 * 3.14 * x  # p = 2*pi*x=radius
    return(p)

# gets radius number from the user, calls a function to calculate the hekef using radius, then prints the hekef:
x = float(input("Enter radius number: "))
p = calchekef (x)
print('the hekef is:', p)
