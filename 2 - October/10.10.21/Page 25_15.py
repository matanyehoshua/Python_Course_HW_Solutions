# Page 25_15

# inputs a number
x = int(input('enter a number: '))
original_number = x
opposite_number = 0

# cheecks if the entered number is different than zero, then starts to take its digits out one by one
# and stores those digits
while x != 0:
    opposite_number = opposite_number * 10 + (x % 10)
    x = x // 10

# prints the opposite number and checks if the number is a palindrome, then prints if it is or not
print(f'opposite number is: {opposite_number}')
print(f'is the number entered a palindrome? {original_number == opposite_number}')