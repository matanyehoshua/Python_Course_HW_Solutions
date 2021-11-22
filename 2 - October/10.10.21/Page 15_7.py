# Page 15_7
x = int(input("Enter a number: "))
count = 0

# checks if the number entered is not zero
if x != 0:
    for i in range(3):
        count = x % 10
        x = x // 10

#prints the meot if the number is atleast 100
if count == 0:
    print ("the number shouldn't be less than 100")
else:
    print ('the meot is ', count)