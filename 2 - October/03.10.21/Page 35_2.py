# Ex. N2
_sum = int(input("Enter a Number: "))
tickets = 1

# Checks if the last numberr entered is equal to the sum
while tickets <= 999:
    last_number = int(input("Enter a Number: "))
    if last_number == _sum:
        break
    else:
        _sum = _sum + last_number
        tickets = tickets + 1

# Prints the sum or tells that "No Sum Found"
if last_number == _sum:
    _sum = _sum + last_number
    print ("The Sum is: ", _sum)
else:
    print("No Sum Found")




