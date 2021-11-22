# HW Q2

# create popByValue function which gets a dictionary and a value as a parameter-
# pop all items with the value. *etgar: returns these items in a list
_list1 = []
_list2 = []
_dict = {}

def popByValue(k, v):
    _dict = {k, v}
    _list1 = [k, v]
    _list2 = [print(k, v) for key in range(k, v)]
    return (_list2)







# user inputs a key and value for the dictionary
k = input("please enter a dictionary key: ")
v = input("please enter a dictionary value: ")
popByValue(k, v)

