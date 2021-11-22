#didn't manage to solve this:
num = int(input("Enter a Number: "))
i = 1
b = 0

for i in range(1, num):
    a = num // i
    if a != b:
        print (a)
        b = a
    else:
        continue