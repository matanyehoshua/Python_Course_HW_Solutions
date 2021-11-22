# Page 18_5

# inputs 2 numbers
x = int(input("enter a number: "))
y = int(input("enter a number: "))

# checks which number is big and sorts it by small > big, otherwise says both are equal
if y > x:
    print (f'the numbers are sorted from small to big {x}, {y}')
elif x > y:
    print (f'the numbers are sorted from small to big {y}, {x}')
else:
    print (f'both number are equal {x}, {y}')