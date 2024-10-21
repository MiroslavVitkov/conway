#!/usr/bin/env python

'''
Deviations:
    - the universe is not infinite, it's a square, beyond it is only death
    - it was a zero-player game for the reasons it was conceived but obviously not here
'''


BOARD_SIZE = 8
NOTHING = '.'
SOMETHING = 'K'


board = [[NOTHING] * BOARD_SIZE for _ in range(BOARD_SIZE)]  # indexing: (row, col)


# --- The 3 rules!
def underpopulation():
    '''
    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    '''
    return False


def overpopulation():
    '''
    Any live cell with more than four live neighbours dies, as if by overpopulation.
    '''
    return False


def zombies():
    '''
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    '''
    return False


alive = input('Please list alive cells e.g. (2,3), (  30,    1 ): ')
board[3][4] = SOMETHING



for row in board:
    for c in row:
        print(c, end='')
    print()
