# Page 25_13

# enters a number and a digit
x = int(input("enter a number: "))
dig = int(input("enter a single digit number"))
count = 0

# counts how many times the digit appears
while x !=0:
    y = x % 10
    x = x // 10
    if y == dig:
        count += 1

# prints the amount of times that digit appears
print(f'the amount the digit appears in the number is: {count}')