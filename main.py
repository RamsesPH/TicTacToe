##  The following is my attempt to tackle the TIC TAC TOE Game - TEXT VERSION 2.0

# Require Modules
import os

# ----- Variables

game_is_on = True           # to test weather the game will continue or not
current_player = "X"        # The player that will start the game
winner = None               #
position = None             # board positioning value
start_game = True           # to see if players want another round of the game
correct_choice = False      # while loop to avoid over writing X or O on the board


# ----- Defining the positioning dictionary
places = {1: '1', 2: '2', 3: '3', 4: '4',
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

# ----- Defining Tic Tac Toe Functions

def clearScreen():
    """This function should clear the window """
    # For windows OS
    if os.name == 'nt':
        os.system('cls')
    # For Posix ( Linux, OSX)
    else:
        os.system('clear')

def drawBoard(places):
    """Takes the Key-value of the Dictionary places and add them to the board  f string below
        in order to draw the board."""

    the_board = (f'| {places[1]} | {places[2]} | {places[3]} |\n--------------\n'
                 f'| {places[4]} | {places[5]} | {places[6]} |\n--------------\n'
                 f'| {places[7]} | {places[8]} | {places[9]} |'
                 )
    print()
    print(the_board)
    print()


# handle player's  turn

def player_X():
    global position
    position = int(position)
    places[position] = 'X'
    return

def player_O():
    global position
    position = int(position)
    places[position] = 'O'
    return

def check_player():
    global current_player
    if current_player == 'X':
        player_X()
    else:
        player_O()

def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return current_player

# ----- checking for a winner

def check_rows():
    global game_is_on
    # check for winning row
    row1 = places[1] == places[2] == places[3]
    row2 = places[4] == places[5] == places[6]
    row3 = places[7] == places[8] == places[9]
    if row1 or row2 or row3:
        game_is_on = False
    if row1:
        return places[1]
    elif row2:
        return places[2]
    elif row3:
        return places[3]
    return

def check_columns():
    global game_is_on
    # check for winning column
    col1 = places[1] == places[4] == places[7]
    col2 = places[4] == places[5] == places[8]
    col3 = places[3] == places[6] == places[9]
    if col1 or col2 or col3:
        game_is_on = False
    if col1:
        return places[1]
    elif col2:
        return places[4]
    elif col3:
        return places[9]
    return

def check_diagonals():
    global game_is_on
    # check for winning diagonal
    diag1 = places[1] == places[5] == places[9]
    diag2 = places[3] == places[5] == places[7]
    if diag1 or diag2:
        game_is_on = False
        return places[5]
    return

def is_a_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diag_winner = check_diagonals()
    if row_winner:
        winner = check_rows()
    elif column_winner:
        winner = check_columns()
    elif diag_winner:
        winner = check_diagonals()
    else:
        winner = None

def is_a_draw():
    pass
    # if len(places[X]) + len(places[O]) == 9:
    #     print("game over")



def is_game_over():
    is_a_win()
    is_a_draw()

# ----- playing the game

def play_the_game():
    global game_is_on
    global start_game
    global position
    drawBoard(places)
    print(f'\nIt is PLAYER {current_player} turn ')
    print()
    applicable = True
    while applicable:
        position = input("\nCHOOSE an unused POSITION from 1 to 9 [print q to quit]: ")
        # checking for correct input
        if position == 'q':
            print("\nYou have chosen to Quit the game, thanks for playing !! Goodbye!")
            game_is_on = False
            start_game = False
            exit()

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("You must CHOOSE a position from 1 to 9, try again: ")
        position = int(position)
        if places[position] == 'X' or places[position] == 'O':
            print("The position is taken, please try again")
        else:
            return position

while start_game:
    # welcome statement
    print('\n'*10)
    print("----------#----------# ---------- #----------# ----------# ------------ #----------")
    print()
    print('Welcome to the Tic Tac Toe game Version 2.0 by Pedro Hernandez\n')
    print()
    print(" The X player starts the game")
    print()
    print("----------# ----------# ----------# ----------# ----------# ------------# ----------")

    # Play The Game

    while game_is_on:
        play_the_game()
        check_player()
        is_game_over()
        change_player()


    # ----- Result
    if winner == 'X' or winner == 'O':
        print(f'\nPlayer {winner} has won, congratulations !!')
    else:
        print('\nIt is a draw!, Nobody Wins !!! ')

    # Start another game ?
    another_game = input("\nDo you want to play the game again?, [ type y for yes and n for no] :  ")
    if another_game == 'y':
        clearScreen()
        start_game = True
    else:
        print("\nThe Game has ended. Goodbye !!!")
        start_game = False

