#didn't manage to solve this:
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))
i = 1
b = 0

if num1 > num2:
    num1 = num2
else:
    for i in range(1, num1):
        a = num1 // i
        b = num2 // i
        if a == b:
            print (a, b)
        else:
            continue