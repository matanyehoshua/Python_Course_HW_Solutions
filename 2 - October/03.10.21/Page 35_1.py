# Ex. N1

# Entering the first Number
check = 1
x = int(input("Enter a Number: "))

# Checking if last entered number is bigger than the previous number
while check <= 99:
    last_number = int(input("Enter a Number: "))
    if last_number >= x:
        check = check + 1
        x = last_number
    else:
        break

# Printing if the 10 numbers that have been entered are "Sorted" or if not, printing "Not Sorted"
if check == 100:
    print ("Sorted")
else:
    print ("Not Sorted")