# HW Q10

# _list = [1, 5, 7, 8, 100]

_list = [1, 5, 7, 8, 100]
biggest_number = _list[0]

# checks which number is bigger and prints the biggest number in the list
for i in range(len(_list)):
    if biggest_number > _list[i]:
        pass
    else:
        biggest_number = _list[i]
print(f'the biggest number in the list is: {biggest_number}')
