# HW Q1

# create isDictKeysAlpha function which gets a dictionary as a parameter-
# returns true if all the keys are alpha (hint: use isaplhpa)

# checks if the entered key and values for the dictionary are letters only
def isDictKeysAlpha(k, v):
    if k.isalpha() and v.isalpha():
        print("function returns True since both items are letters only")
        return (True)
    else:
        print('enter letters only')


# user inputs a key and value for the dictionary
k = input("please enter a dictionary key: ")
v = input("please enter a dictionary value: ")
isDictKeysAlpha(k, v)
