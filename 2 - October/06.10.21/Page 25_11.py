# Page 25_11

x = int(input("enter a number: "))
sfarot = 0

# checks the number of sfarot
while x != 0:
    x = x // 10
    sfarot = sfarot + 1

# prints sfarot number
print("the number of sfarot is:", sfarot)
