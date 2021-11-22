# I managed to get the first half, but cannot get the second part to answer correctly.
x = int(input('Enter a Number: '))
if x < 10:
    print (x)
else:
    x = (x // 10) + (x % 10)
    print(x)
