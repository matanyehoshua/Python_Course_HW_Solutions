# Page 25_14

# inputs a number
x = int(input("enter a number"))
opposite = 0

# calculates th opposite number
while x != 0:
    opposite = opposite * 10 + (x % 10)
    x = x // 10

print(f'the opposite number is: {opposite}')
