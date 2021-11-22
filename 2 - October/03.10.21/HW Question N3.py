#input numberes from the user until a number that can be divided by 2 without a reminder will be entered (i.e. 4) ,
# then input numbers from the user until a number that can be divided by 3 without a reminder will be entered (i.e. 9),
# then input numbers from the user until a number that can be divided by 4 without a reminder will be entered (i.e. 28) ...
# until you reach 10, then break out of the loop. if the user enters a negative number just ignore it.
# *bonus: if the user enters the same number twice then break out of the loop

last_number = int(input("Enter a Number: "))

while last_number > 0:
    x = int(input("Enter a Number: "))
    if x % 2 == 0 or x == last_number:
        x = int(input("Enter a Number: "))
        if x % 3 == 0 or x == last_number:
            x = int(input("Enter a Number: "))
            if x % 4 == 0 or x == last_number:
                x = int(input("Enter a Number: "))
                if x % 5 == 0 or x == last_number:
                    x = int(input("Enter a Number: "))
                    if x % 6 == 0 or x == last_number:
                        x = int(input("Enter a Number: "))
                        if x % 7 == 0 or x == last_number:
                            x = int(input("Enter a Number: "))
                            if x % 8 == 0 or x == last_number:
                                x = int(input("Enter a Number: "))
                                if x % 9 == 0 or x == last_number:
                                    x = int(input("Enter a Number: "))
                                    if x % 10 == 0 or x == last_number:
                                        break
                                    elif x == last_number:
                                        break


print("Out of loop")

