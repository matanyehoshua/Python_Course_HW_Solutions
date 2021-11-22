# Page 25_12

x = int(input("enter a number: "))
_sum = 0

# calculates the _sum of the input number
while x != 0:
    _sum = _sum + (x % 10)
    x = int(x / 10)

# prints the _sum
print("the sum of sfarot is:", _sum)
