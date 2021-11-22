# HW Q11

# makes a list of each part of a list from the list of lists
list_of_lists = [[4, 8, 200], [4, 3000, -1], [5, 87, 12]]
list1 = list_of_lists[0]
list2 = list_of_lists[1]
list3 = list_of_lists[2]
smallest_number1 = list1[0]
smallest_number2 = list2[0]
smallest_number3 = list3[0]

# takes the smallest number from each list
for i in range(len(list1)):
    if smallest_number1 < list1[i]:
        pass
    else:
        smallest_number1 = list1[i]
for i in range(len(list2)):
    if smallest_number2 < list2[i]:
        pass
    else:
        smallest_number2 = list2[i]
for i in range(len(list3)):
    if smallest_number3 < list3[i]:
        pass
    else:
        smallest_number3 = list3[i]

# checks which number is smaller compared to the other lists and prints the smallest number of all
if smallest_number1 < smallest_number2:
    if smallest_number1 < smallest_number3:
        print(f'the smallest number in the list of lists is: {smallest_number1}')
elif smallest_number2 < smallest_number1:
    if smallest_number2 < smallest_number3:
        print(f'the smallest number in the list of lists is: {smallest_number2}')
else:
    if smallest_number3 < smallest_number1:
        if smallest_number3 < smallest_number2:
            print(f'the smallest number in the list of lists is: {smallest_number3}')