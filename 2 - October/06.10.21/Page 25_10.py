# Page 25_10

x = int(input("enter a number: "))

# checks the most left digit number and prints it
while x != 0:
    while abs(x) >= 10:
        x = x // 10
    print("the most left digit is:", x)
    break
