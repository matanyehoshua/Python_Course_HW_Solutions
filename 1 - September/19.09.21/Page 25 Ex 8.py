# Page 25 Ex 8:


lowest = int(input("Enter a Number: "))
i_min = lowest

while lowest > 0:
    if i_min > lowest:
        i_min = lowest
    else:
        lowest = int(input("Enter a Number: "))

print('The Lowest Positive Number Is=', i_min)