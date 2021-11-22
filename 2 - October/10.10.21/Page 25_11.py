# Page 25_11

# inputs a number
x = int(input("enter a number: "))
digits = 1

# checks if the number is above 9 and adds its digits sum
while x > 9:
    x = x // 10
    digits += 1

# print the amount of the digits the number has
print(f'the total digits of the number is: {digits}')
