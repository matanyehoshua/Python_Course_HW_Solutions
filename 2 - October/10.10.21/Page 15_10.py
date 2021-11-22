# Page 15_10

x = float(input("Enter a number: "))

# checks if the number can be divided by two without remainder, if so prints it, otherwise adds 1 and checks again
# if it can be divided without remainder it prints it, otherwise adds another 1, and if still not then another 1
# then prints the number
if x % 2 == 0:
    print(int(x))
else:
    x = int(x)
    x += 1
    if x % 2 == 0:
        print(int(x))
    else:
        x += 1
        if x % 2 == 0:
            print(int(x))
        else:
            x += 1
            print(int(x))