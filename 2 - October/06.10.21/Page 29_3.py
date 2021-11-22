# Page 29_3
_sum = 0

# calculates the sum of digits of given number

x = int(input("enter a number: "))
if x < 0:
    print("not a positive number")
else:
    while x != 0:
        _sum = _sum + (x % 10)
        x = int(x / 10)

    print ("the sum of sfarot is", _sum)