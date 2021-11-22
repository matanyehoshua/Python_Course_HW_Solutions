# Python Project N1
# word guessing game
# libraries to import:
import random

# main expression list
expression_list = ['always', 'be', 'yourself'], ['do', 'your', 'best'], ['focus', 'and', 'win'], ['keep', 'it', 'cool'],\
                  ['life', 'is', 'awesome'], ['never', 'give', 'up'], ['yes', 'you', 'can'], ['go', 'for', 'it'],\
    ['focus', 'and', 'win'], ['change', 'is', 'good']
# blank expression list
blank_expression_list = ['______', '__', '________'], ['__', '____', '____'], ['_____', '___', '___'], ['____', '__', '____'],\
                  ['____', '__', '_______'], ['_____', '____', '__'], ['___', '___', '___'], ['__', '___', '__'],\
    ['_____', '___', '___'], ['______', '__', '____']


a = random.randint(0, 9)
print(f'{blank_expression_list[a]}')
main_blank_expression_list = blank_expression_list[a]
main_expression_list = expression_list[a]
print(f'{main_expression_list}')
list(main_expression_list)
for i in main_expression_list:
    for j in i:
        letter = input("enter a letter: ")
        if letter == j:
           y = main_blank_expression_list.replace("_", letter)









