
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
    print(" ")
    print(" ")
    

# Function that allows the player to input their move
def player_input(board, player):
    
    while True:
        move = input(f"Player {player}, enter your move (q, w, e, a, s, d, z, x, c): ").lower()
        if move in board and board[move] == " ":
            board[move] = player
            break
        elif move == "restart":
            run_tic_tac_toe()
        else:
            print("Move is invalid. Please select an appropiate move.")


# This function will check if there is a winner after the move.
def check_winner(board, player):

    winning_combinations = [
        {'q', 'w', 'e'},  # Top row
        {'a', 's', 'd'},  # Middle row
        {'z', 'x', 'c'},  # Bottom row
        {'q', 'a', 'z'},  # Left column
        {'w', 's', 'x'},  # Middle column
        {'e', 'd', 'c'},  # Right column
        {'q', 's', 'c'},  # Diagonal from top left to bottom right
        {'e', 's', 'z'}   # Diagonal from top right to bottom left
    ]

    current_positions = {key for key, value in board.items() if value == player}

    # The loop will iterate through the combinations in winning_combinations and check if the current position,
    # which is saved in the dictionary, matches any of them. 

    for combination in winning_combinations:
        if combination.issubset(current_positions):
            return True
        
    # notice how the return false is outside the loop. 
    return False


def check_draw(board):
    return all(value != " " for value in board.values())

# Play again function
def play_again():
    play_again = input("Would you like to play again (Y or N)?").lower()
    if play_again == "y":
        run_tic_tac_toe()
    elif play_again == "n":
        pass
    else:
        print("Please enter a valid response. Y or N?")

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
            play_again()
            break

        if check_draw(board):
            print_board(board)
            print("Game is a draw!")
            play_again()
            break

        # Change players
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

run_tic_tac_toe()


