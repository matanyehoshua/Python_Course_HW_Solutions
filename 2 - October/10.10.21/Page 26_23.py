# page 26_23

# inputs a number
x = int(input("enter a number: "))
num = 1

# checks if the number is divisible without a remainder, then prints the numbers that are divisible without remainder
for i in range (x):
    if x % num == 0:
        print (f'{num} ', end='')
    num += 1


