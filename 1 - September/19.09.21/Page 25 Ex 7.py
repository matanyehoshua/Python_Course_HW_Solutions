# Page 25 Ex 7:


top = int(input("Enter a Number: "))
i_max = top

while top > 0:
    if i_max < top:
        i_max = top
    else:
        top = int(input("Enter a Number: "))

print('The Top Positive Number Is=', i_max)