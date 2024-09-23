
"""
TIC TAC TOE
"""

"""


"""

# Function that will keep the board updated according to moves.
def print_board(board):
    print(" ")
    print(" ")
    print(f" {board['q']} | {board['w']} | {board['e']} ")
    print("---+---+---")
    print(f" {board['a']} | {board['s']} | {board['d']}")
    print('---+---+---')
    print(f" {board['z']} | {board['x']} | {board['c']}")
    

# Function that allows the player to input their move
def player_input(board, player):
    move = input(f"Player {player}, enter your move (q, w, e, a, s, d, z, x, c): ".lower())
    if move in board and board[move] == " ":
        board[move] = player
    else:
        return "Move is invalid. Please select an appropiate move."

# This function will check if there is a winner after the move.
def check_winner(board, player):

    winning_combinations = [
        {'q', 'w', 'e'},
        {'a', 's', 'd'},
        {'z', 'x', 'c'},
        {'q', 'a', 'z'},
        {'w', 's', 'x'},
        {'e', 'd', 'c'},
        {'q', 's', 'c'},
        {'z', 's', 'e'}
        ]

    current_positions = {key for key, value in board.items() if value == player}

    for combination in winning_combinations:
        if combination.issubset(current_positions):
            return True
        else:
            return False
        
def check_draw(board):
    return all(value != " " for value in board.values())

def run_tic_tac_toe():

    # Initializing empty board
    board = {'q':' ', 'w':' ', 'e':' ', 'a':' ', 's':' ', 'd':' ', 'z':' ', 'x':' ', 'c':' ',}

    current_player = "X"

    while True:

        print_board(board)

        player_input(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("Game is a draw!")
            break

        # Change players
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

run_tic_tac_toe()


