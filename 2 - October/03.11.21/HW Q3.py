# HW Q3

# create compareDict function which gets two dictionaries as parameters-
# returns True if all keys+values are similar between dictionaries otherwise returns False


# compares the keys and values between dictionaries
def compareDict(k1, v1, k2, v2):
    if k1 == k2 and v1 == v2:
        print("dictionaries are the same, returning True")
        return True
    else:
        print("dictionaries are different, returning False")
        return False


# user inputs two dictionaries
print("enter two dictionaries")
k1 = input("please enter a dictionary key: ")
v1 = input("please enter a dictionary value: ")
k2 = input("please enter another dictionary key: ")
v2 = input("please enter another dictionary value: ")
compareDict(k1, v1, k2, v2)