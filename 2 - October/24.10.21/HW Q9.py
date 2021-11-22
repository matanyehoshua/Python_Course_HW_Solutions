# HW Q9

# _list [8, 1000, -3, 2, 5]

_list = [8, 1000, -3, 2, 5]
_sum = 0
_objects = 0
_smaller_than_avg = []

# calculates and prints the sum of the list
for i in range(len(_list)):
    _sum += _list[i]
    _objects += 1
print(f'the sum of the list is: {_sum}')
# prints the highest value in the list
print(f'the highest value number is: {max(_list)}')
# prints the lowest value in the list
print(f'the lowest value number is: {min(_list)}')
# prints the avg of the numbers in the list
print(f'the avg of the numbers is: {_sum / _objects}')
# prints the list without the middle item
_new_list = _list[0:2] + _list[3:]
print(f'the list without the middle item is: {_new_list}')
# sorts the list
_newer_list = _list
_newer_list.sort()
print(f'the sorted list is: {_newer_list}')
# multiplies the list by 5 times
newest_list = _list * 5
print(f'the list 5 times is: {newest_list}')
# prints the list without the first item
_list_second_to_last = _list[1:]
print(f'the list without the first item is: {_list_second_to_last}')
# prints the numbers in the list that are smaller than the avg of the numbers in the list
for i in range(len(_list)):
    if _list[i] < 202.4:
        _smaller_than_avg.append(_list[i])
print(f'the smaller than avg numbers are:{_smaller_than_avg} ')

