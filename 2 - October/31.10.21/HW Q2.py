# HW Q2

# some_list = [1,4,7,12,19,22, 23, 26].
# create of list of string for even or odd: in this case
# [‘1 is odd’, ‘4 is even’, ‘7 is odd’ …] using list comprehension
some_list = [1,4,7,12,19,22, 23, 26]

# takes the list and checks which number is even or odd and prints the correct answer
print([f'{x} is {"even" if x % 2 == 0 else "odd"}' for x in some_list])