#4. input a number from the user
#     check if the number ahadot and asarot digit are equal
#     you MUST use 1 if (+and)
a = int(input('Enter a Number'))

if a % 10 == a // 10:
    print('Equal')
else:
    print('Not Equal')