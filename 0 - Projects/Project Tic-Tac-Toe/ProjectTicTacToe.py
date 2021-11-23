# Python Tic Tac Toe project
# libraries to import
# this game features a one player vs computer mode

import random

# the board basic blank setup
theboard = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# function to reset the board (when game is over)
def reset_board(theboard):
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    return board

# function that checks if the number entered is actually a number and not a letter for the row section
def check_row(row):
    row = input('input row number, 0-2 only')
    if row.isdigit():
        row = int(row)
        return row
# function that checks if the number entered is actually a number and not a letter for the col section
def check_col(col):
    col = input('input row number, 0-2 only')
    if col.isdigit():
        row = int(col)
        return col
# function that prints the board to the player
def printboard(theboard):
    for i in range(3):
        print(end='\n')
        for j in range(3):
            print(theboard[i][j], end='')
# main function of game, where all the main code is stored
def main():
    print(f'Welcome to Tic-Tac-Toe! in this game you play against the computer! Good Luck! \
You are player "X", while the computer is player "O"')
    theboard = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    turn = 'X'
    count = 0
    for i in range(10):
        printboard(theboard) # prints the board
        print("\nIt's your turn," + turn + ".Move to which place?")
        row = input('input row number, 0-2 only') # user inputs row number from 0-2
        if row.isdigit():
            row = int(row)
        else:
            print('you must select a number between 0-2!')
            row = check_row(row)
        col = input('input col number, 0-2 only') # user inputs col number from 0-2
        if col.isdigit():
            col = int(col)
        else:
            print('you must select a number between 0-2!')
            col = check_col(col)
        if theboard[row][col] == '_':
            turn = 'X'
            theboard[row][col] = 'X'
            count += 1
        else:
            # message that shows when user or computer have used a used space on the board
            print("That place is already filled.\nMove to which place?")
            turn = 'O'
        if count < 3:
            if turn == 'X':
                turn = 'O'
            elif turn == 'O':
                turn = 'X'
            else:
                turn = 'X'
        printboard(theboard)
        print("It's your turn," + turn + ".Move to which place?")
        # computer turn - is randomly generated
        row = int(random.randint(0, 2))
        col = int(random.randint(0, 2))
        if theboard[row][col] == '_':
            turn = 'O'
            theboard[row][col] = 'O'
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            turn = 'X'
        if count < 3:
            if turn == 'O':
                turn = 'X'
            elif turn == 'X':
                turn = 'O'
            else:
                turn = 'O'
        # the game checks who won after 3 turns
        if count >= 3:
            if theboard[0][0] == theboard[0][1] == theboard[0][2] != '_':  # across the top
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theboard[1][0] == theboard[1][1] == theboard[1][2] != '_':  # across the middle
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theboard[2][0] == theboard[2][1] == theboard[2][2] != '_':  # across the bottom
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theboard[0][0] == theboard[1][0] == theboard[2][0] != '_':  # down the left side
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theboard[0][1] == theboard[1][1] == theboard[2][1] != '_':  # down the middle
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theboard[0][2] == theboard[1][2] == theboard[2][2] != '_':  # down the right side
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theboard[0][0] == theboard[1][1] == theboard[2][2] != '_':  # diagonal from top left to bottom right
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theboard[0][2] == theboard[1][1] == theboard[2][0] != '_':  # diagonal from top right to bottom left
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
                # If neither X nor O wins and the board is full, we'll declare the result as 'tie',
                # also when game is over the game  asks if the player wants to start a new game.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            restart = input("Do want to play Again?(y/n)")
            if restart == "y" or restart == "Y":
                theboard = reset_board(theboard)
                main()
    # when game is over the game  asks if the player wants to start a new game
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        theboard = reset_board(theboard)
        main()
    else:
        # in-case the player types anything else but 'y' or 'Y' the program ends
        print(f'Thank you for playing!')

# the program starts here and calls to the main function
main()