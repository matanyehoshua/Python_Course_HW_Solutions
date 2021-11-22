# Page 15_8

x = int(input("Enter a number "))
count = 0

# combines the value of the sfarot and stores it in count
for i in range(2):
    count += x % 10
    x = x // 10

# prints the sum of sfarot
print ('the sum of sfarot is: ', count)