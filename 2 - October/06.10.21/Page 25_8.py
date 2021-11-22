# Page 25_8

x = int(input("Enter a Number: "))
low_positive = x

# Checks if the number is above 0
while x > 0:
    if low_positive > x:
        low_positive = x
    else:
        x = int(input("Enter a Number: "))
        if x <= 0:
            break

# Prints the lowest positive number or tells that the number is not positive
if low_positive < 0:
    print("the lowest positive number is not positive:", low_positive)
else:
    print("the lowest positive number is:", low_positive)


