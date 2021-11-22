# Page 38_8

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

# prints the row x times and how many each row y times:
for i in range(x):
    for i in range(y):
        print ('*', end = ' ')
    print()

