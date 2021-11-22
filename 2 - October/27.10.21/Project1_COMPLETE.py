# Python Project N1
# word guessing game
# libraries to import:
import random
import time
a = random.randint(0, 9)
score = 0
attempts = 0
errors = 0
blank_letter_count = 0

# function that checks bonus points, if game was completed in less than 30 seconds
def bonus_points(time):
    if time <= 30:
        return(100)
    else:
        return(0)


# main expression list
print(f'Welcome to the word guessing game! Please fill all the empty letters, Good Luck!')
expression_list = ['always', 'be', 'yourself'], ['do', 'your', 'best'], ['focus', 'and', 'win'], ['keep', 'it', 'cool'],\
                  ['life', 'is', 'awesome'], ['never', 'give', 'up'], ['yes', 'you', 'can'], ['go', 'for', 'it'],\
    ['focus', 'and', 'win'], ['change', 'is', 'good']
# blank expression list
expression_list = expression_list[a]
blank_expression_list = ['_' * len(word) for word in expression_list]
for x in blank_expression_list:
    for s in x:
        blank_letter_count += 1
# prints the blank expression list
print(blank_expression_list)
# starts counting the time (for bonus points at the end)
time_start = time.time()
# gets a letter from the user and fills the missing letters with correct letters
while True:
    letter = input("enter a letter: ")
    attempts += 1
    print(attempts)
    for i in range(len(expression_list)):
        new_word = ''
        for j in range(len(expression_list[i])):
            if expression_list[i][j] == letter:
                new_word += letter
            else:
                new_word += blank_expression_list[i][j]
        blank_expression_list[i] = new_word
        print()
    print(blank_expression_list)
# checks if the expression is complete, then it calculates the score
    if blank_expression_list == expression_list:
        if attempts > blank_letter_count:
            errors = -attempts + blank_letter_count
            score = blank_letter_count * 5 + errors
            time_end = time.time()
            z = time_end - time_start
            print(f'your error count is: {errors}')
            print(f'your score is: {score}')
            print(f'time taken to complete: {int(time_end - time_start)} seconds')
            bonus_points(int(z))
            score += bonus_points(z)
            if bonus_points(z) > 0:
                print(f'congratulations, you have completed the word guessing game in less than 30 seconds!, \
and you won 100 bonus points!')
                print(f'your total score is: {score}')
                break
        else:
            score = blank_letter_count * 5
            time_end = time.time()
            z = time_end - time_start
            print(f'your error count is: {errors}')
            print(f'your score is: {score}')
            print(f'time taken to complete: {int(time_end - time_start)} seconds')
            bonus_points(int(z))
            score += bonus_points(z)
            if bonus_points(z) > 0:
                print(f'congratulations, you have completed the word guessing game in less than 30 seconds!, \
and you won 100 bonus points!')
                print(f'your total score is: {score}')
                break