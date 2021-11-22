#3. input a number from the user
#     check if the number has 2 digits, if so print the ahadot digit
#     you MUST use 1 if (+and)
a = int(input('Enter A number'))

if a > 9:
    a = a % 10
    print(a)