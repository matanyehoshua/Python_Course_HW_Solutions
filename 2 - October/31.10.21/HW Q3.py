# HW Q3

# *etgar: list1 = [1,2] ; list2 = [4,5].
# create a list of tuples [(1,4), (1,5), (2,4), (2, 5)] using list comprehension
list1 = [1, 2]
list2 = [4, 5]

# prints the list of tuples of the given numbers
print([(items_list1, items_list2) for items_list1 in list1 for items_list2 in list2])