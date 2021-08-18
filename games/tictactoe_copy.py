from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

the_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def player_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input("Do you want to be X or O?").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position]= marker

def win_check(board, mark):
    if board[1] == mark and board[2]==mark and board[3]==mark:
        print("We have a winner!")
        return True
    if board[4] == mark and board[5]==mark and board[6]==mark:
        print("We have a winner!")
        return True
    if board[7] == mark and board[8]==mark and board[9]==mark:
        print("We have a winner!")
        return True
    if board[1] == mark and board[4]==mark and board[7]==mark:
        print("We have a winner!")
        return True
    if board[2] == mark and board[5]==mark and board[8]==mark:
        print("We have a winner!")
        return True
    if board[3] == mark and board[6]==mark and board[9]==mark:
        print("We have a winner!")
        return True
    if board[1] == mark and board[5]==mark and board[9]==mark:
        print("We have a winner!")
        return True
    if board[3] == mark and board[5]==mark and board[7]==mark:
        print("We have a winner!")
        return True
    else:
        return False


def first_player():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):

    for x in range(1,10):
        if space_check(board,x):
            return False
    return True


def player_choice(board):
    
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):

        position = int(input("Enter a value from 1 to 9: "))
        
    return position

def replay():
    choice = "wrong"
    while choice not in ['Y' ,'N']:
        choice = input("Do you want to continue playing? (Enter Y or N)")
        if choice not in ['Y','N']:
            print("Sorry, invalid choice! Please enter Y or N...")
    if choice == "Y":
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')

while True:
    
    the_board = [' ']*10
    
    
    
    player1_marker, player2_marker = player_input()

    turn = first_player()
    print(turn + ' will go first...')
    
    play_game = input('Ready to play? Y or N?').upper()
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_boardlay_board(the_board)
                    print('TIME GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'
            
    if not replay():
        break

