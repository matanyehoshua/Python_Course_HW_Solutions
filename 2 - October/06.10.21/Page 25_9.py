# page 25_9

numbers = 1
i = 0
x = int(input("Enter a number: "))
top_number = x

# Checks the position of the top number
while i < 5:
    x = int(input("Enter a number: "))
    if x > top_number:
        top_number = x
        numbers = numbers + 1
        i = i + 1
    else:
        i = i + 1

# Prints the top number position
print ("The Top number position is:", numbers)
