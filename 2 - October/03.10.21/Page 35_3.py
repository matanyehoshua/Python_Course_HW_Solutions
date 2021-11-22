# Ex. N3
tickets = 1

# Check to see if Data is Correct
while tickets <= 364:
    last_number = int(input("Enter a Number: "))
    if last_number < -5 or last_number > 40:
        break
    tickets = tickets + 1

# Prints "Data input is OK" when all Data received is correct, otherwise prints "Data input is not OK"
if tickets == 365:
    print ("Data input is OK")
else:
    print("Data input is not OK")

