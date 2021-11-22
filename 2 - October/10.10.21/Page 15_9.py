# Page 15_9

x = int(input("Enter a number"))
count = 0

# takes the ahadot, multiplies it by 10 and adds the asarot as ahadot, then prints the result
count = x % 10
x = x // 10
count *= 10
count += x % 10
# prints the entered number in reverse
print('the reverse number value is: ', count)