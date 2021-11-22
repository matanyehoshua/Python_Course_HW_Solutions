# Page 15_6

x = int(input("Enter a number: "))

# stores the asarot in 'count' then prints it
for i in range(2):
    count = x % 10
    x = x // 10

print(count)
