#!/usr/bin/env python


'''
Deviations:
    - the universe is not infinite, it's a square, beyond it is only death,
    - it was a zero-player game for the reasons it was conceived but times they are changing.

Remember new board is calculated over old board and only then applied.
'''


# --- The 3 rules.
def underpop():
    '''
    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    '''
    return False


def overpop():
    '''
    Any live cell with more than four live neighbours dies, as if by overpopulation.
    '''
    return False


def zombies():
    '''
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    '''
    return False
