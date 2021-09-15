# Command                      Description
# Human Game                   Start a two player game
# Computer Game                Start a game against the computer
# Random Game                  Start a random simulation


import sys
import XOGame

if len(sys.argv) >1:
    board = XOGame.empty_board
    cmd = sys.argv[1]
    if cmd == 'Human':
        XOGame.human_game(board)
    elif cmd == 'Computer':
        XOGame.human_vs_computer_game(board)
    elif cmd == 'Random':
        XOGame.random_game(board)
