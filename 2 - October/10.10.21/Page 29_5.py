# page 29_5

# takes a number above 1
x = int(input("enter a number above 1: "))
num = 4

# checks if the number is a Prime number, if its not, it will keep getting new numbers
while x > 1:
    if x % 2 != 0:
        print('Prime number')
        break
    else:
        x = int(input("enter a number: "))

# prints the non prime numbers until the number entered
for i in range (4, x-1, 2):
    numbers = x / num
    print (f'{num}, ', end='')
    num += 2
