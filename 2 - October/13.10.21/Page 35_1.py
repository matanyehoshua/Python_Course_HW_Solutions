# Page 35_1

x = int(input("Enter a sorted number"))
counter = 1

# checks if the numbers entered are sorted and prints "Sorted!", otherwise prints "Not Sorted!"
for i in range (99):
    last_number = int(input("Enter a sorted number"))
    if last_number >= x:
        x = last_number
        counter += 1
        if counter == 100:
            print ("Sorted!")
    else:
        print("Not Sorted!")
        break
