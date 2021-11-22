# Page 26_19

# inputs a number
x = int(input("enter a number: "))
azeret = x
num = 1

# calculates the azeret
for i in range (x-1):
    azeret = azeret * num
    num += 1

# prints the azeret
print (f'the azeret is:{azeret} ')
