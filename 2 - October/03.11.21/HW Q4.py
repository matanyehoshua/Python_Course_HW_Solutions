# HW Q4

# create newDict function which gets two list1 and list2 as parameter-
# returns a dictionary which consist of the two lists: list1 will be the keys and list2 will be the values.
# if the lists are not in the same length or list1 contains duplication returns None
list1 = []
list2 = []

# checks if the lists are not equal or different in length, then prints the two lists as a single dictionary
def newDict(list1, list2):
    if list1 == list2:
        print('the lists are duplicated')
        return (None)
    elif len(list1) != len(list2):
        print('the lists are not in the same length')
        return (None)
    else:
        _newDict = {list1: list2}
        print(f'the new dictionary is {_newDict}')
        return (_newDict)

# user inputs 2 lists
print("please enter two lists: ")
list1 = input("enter a first list")
list2 = input("enter a second list")
newDict(list1, list2)


