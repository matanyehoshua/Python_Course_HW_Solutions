# HW_5
# same as question 4- but make three rounds , and print the highest score between the 3 rounds

import random

# takes a random number from 1 to 100 including 100, and checks if the user entered number is the guessed number
# if the number is too high, prints: "too high", if it is too low, then prints "too low"
# if the number is corrent, prints bingo and shows the number of guesses it took to guess the corrent number
# does this whole thing for 3 times and then prints the lowest amount of guesses that hit the number
def bingo():
    count = 0
    top_score = 0
    for i in range(3):
        count += 1
        x = random.randint(1, 100)
        guesses = 0
        for i in range(1000):
            y = int(input("enter a number: "))
            guesses += 1
            if y > x:
                print("too high")
            elif y < x:
                print("too low")
            else:
                print("bingo, you guessed the corrent number!")
                print(f'it took you {guesses} tries')
                break
        if count == 3:
            top_score = guesses
            print(f'your best score is: {top_score}')
        elif top_score == 0 or guesses < top_score:
            top_score = guesses
# calls the function
bingo()
