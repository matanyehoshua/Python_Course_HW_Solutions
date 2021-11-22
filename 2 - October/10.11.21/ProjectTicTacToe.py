# Project 2 Tic Tac Toe
import random

board = [['_','_','_'],['_','_','_'],['_','_','_']]

def get_player_choice(is_computer):
    # turn == 0 = player turn, turn == 1 = computer turn
    if not is_computer == 1:
        get_row = input('Please enter row: ')
        get_col = input('Please enter col: ')
        if not board[get_row][get_col] == '_':
            print(f'please choose a free space on the board!')
            get_player_choice()
        board[get_row][get_col] = 'X'
        return 1
    else:
        get_row = random.randint(1,3)
        get_col = random.randint(1,3)
        if not board[get_row][get_col] == '_':
            print(f'Computer selected a taken space on the board')
            get_player_choice()
        board[get_row][get_col] = 'O'
        return 0

def check_if_won():
    for k in range(board):



def present_board():
    for i in range(3):
        print(end='\n')
        for j in range(3):
            print("_", end='')




def play_game():
    game_over = False
    while not game_over:
        present_board()
        player1_choice = get_player_choice(0)
        check_if_won()
        if this_is_draw():
            break
        player2_choice = get_player_choice() # O
        check_if_won()


def main():
    print(f"Welcome to Tic-Tac-Toe! Enjoy the game! the first player is 'X', the second player is 'O'")
    play_game()

main();