
"""
TIC TAC TOE
"""

"""
All winning combinations:

I need a way to keep track of the board.

A way to store winning combinations.

Steps to playing:
Empty board. 
Player 1 enters their choice.
Choice is entered into the dictionary.
The new board updates.
The game checks for winners.
If no winner, player 2 gets opportunity to enter next choice. 

"""
# Here we store our values in a dictionary
board = {'q':' ', 'w':' ', 'e':' ', 'a':' ', 's':' ', 'd':' ', 'z':' ', 'x':' ', 'c':' ',}

# Here are the winning combinations
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

# Function that will keep the board updated according to moves.
def print_board(board):
    print(f" {board['q']} | {board['w']} | {board['e']} ")
    print("---+---+---")
    print(f" {board['a']} | {board['s']} | {board['d']}")
    print('---+---+---')
    print(f" {board['a']} | {board['s']} | {board['d']}")

# 