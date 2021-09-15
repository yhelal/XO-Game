# Noughts and Crosses

import random


h1 = [0, 1, 2]
h2 = [3, 4, 5]
h3 = [6, 7, 8]
v1 = [0, 3, 6]
v2 = [1, 4, 7]
v3 = [2, 5, 8]
d1 = [0, 4, 8]
d2 = [2, 4, 6]
lines = [h1, h2, h3, v1, v2, v3, d1, d2]
empty_board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']



def print_board(b):
    for n, x in enumerate(b):
        print(x, end='')
        if (n+1) % 3 == 0:
            print('')


def full(b):
    if '_' not in b:
        return True
    else:
        return False



def wins(p, b):
    win = [p, p, p]
    for l in lines:
        bl = [b[x] for x in l]         # list comprehension
        if bl == win:
            return True
    return False


def random_move(b, p):
    played = False
    while not played:
        r = random.randint(0, 8)
        if b[r] == '_':
            b[r] = p
            played = True


def random_game(b):
    while not full(b):
        random_move(b, 'x')
        print_board(b)
        print('')
        if wins('x', b):
            print('x has won')
            return
        if full(b):
            print("It's a draw!")
            return
        random_move(b, 'o')
        print_board(b)
        print('')
        if wins('o', b):
            print('o has won')
            return
        if full(b):
            print("It's a draw!")
            return


def human_move(b, p):
    valid = False
    while not valid:
        pos = input(f'Player {p} enter a position from 0 to 8: ')
        if not pos.isdigit():
            print('Not a valid board position')
        elif int(pos) > 8 or int(pos) < 0 :
            print('Board position must be between 0 and 8')
        elif b[int(pos)] == '_':
            valid = True
            b[int(pos)] = p
        else:
            print('Position taken')


def human_game(b):
    while not full(b):
        human_move(b, 'x')
        print_board(b)
        print('')
        if wins('x', b):
            print('x has won')
            return
        if full(b):
            print("It's a draw!")
            return
        human_move(b, 'o')
        print_board(b)
        print('')
        if wins('o', b):
            print('o has won')
            return
        if full(b):
            print("It's a draw!")
            return


def try_to_take(b, ps):
    for p in ps:
        if b[p] == '_':
            b[p] = 'x'
            return True
    return False


def tactic_play_centre(b):
    return try_to_take(b, [4])


def win_or_block(b, piece):
    for l in lines:
        bl = [b[x] for x in l]
        if bl.count('_') == 1 and bl.count(piece) == 2:
            for x in l:
                if b[x] == '_':
                    b[x] = 'x'
            return True
    return False


def tactic_win(b):
    return win_or_block(b, 'x')


def tactic_block(b):
    return win_or_block(b, 'o')


def tactic_empty_corner(b):
    return try_to_take(b, [0, 2, 6, 8])


def tactic_empty_sides(b):
    return try_to_take(b, [1, 3, 5, 7])


def tactic_opposite_corner(b):
    l = []
    if b[0] == 'o':
        l.append(8)
    if b[2] == 'o':
        l.append(6)
    if b[6] == 'o':
        l.append(2)
    if b[8] == 'o':
        l.append(0)
    return try_to_take(b, l)


def computer_move(b):
    print('Computer has played: ')
    if tactic_win(b):
        print('Used tactic_win')
        return
    if tactic_block(b):
        print('Used tactic_block)')
        return
    if tactic_play_centre(b):
        print('Used tactic_centre')
        return
    if tactic_empty_corner(b):
        print('Used tactic_empty_corner')
        return
    if tactic_empty_sides(b):
        print('Used tactic_empty_sides')
        return
    if tactic_opposite_corner(b):
        print('Used tactic_opposite_corner')
        return
    print('No tactic applied: error in tactic implementations')


def human_vs_computer_game(b):
    s = 'ch'      # so the starter is random every game
    player = random.choice(s)       # random.choice returns a single random element from a sequence
    while not full(b):
        if player == 'h':
            human_move(b, 'o')
            print_board(b)
            print('')
            if wins('o', b):
                print('Human player has won')
                return
            if full(b):
                print("It's a draw!")
                return
            player='c'
        if player == 'c':
            computer_move(b)
            print_board(b)
            print('')
            if wins('x', b):
                print('Computer has won')
                return
            if full(b):
                print("It's a draw!")
                return
            player = 'h'


board = empty_board
# random_game(board)
# human_game(board)
#human_vs_computer_game(board)



