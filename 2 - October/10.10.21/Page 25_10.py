# Page 25_10

# inputs a number
x = int(input("enter a number: "))

# reduces the other digits until only the most left digit is left
while x > 10:
    x = x // 10

# prints the most left digit
print (f'the most left digit of the number is: {x}')
