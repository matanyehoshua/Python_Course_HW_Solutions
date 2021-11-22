# HW_4

# create a function that generates a random number between 1-100 (=lucky number).
# input numbers from the user until the use will guess the lucky number.
# if the user guesses lower than the lucky number- print: “too low”,
# if the user guesses higher than the lucky number- print “too high”.
# if the user guesses correctly- print “bingo”.
# print how many guesses were made until the “bingo”

# imports a module that has a number randomizer in it
import random

# takes a random number from 1 to 100 including 100, and checks if the user entered number is the guessed number
# if the number is too high, prints: "too high", if it is too low, then prints "too low"
# if the number is corrent, prints bingo and shows the number of guesses it took to guess the corrent number
def bingo():
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

# calls the function
bingo()
