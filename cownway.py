#!/usr/bin/env python

'''
Deviations:
    - the universe is not infinite, it's a square, beyond it is only death
    - it was a zero-player game for the reasons it was conceived but obviously not here
'''

# --- Rules
#    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#    Any live cell with two or three live neighbours lives on to the next generation.
#    Any live cell with more than three live neighbours dies, as if by overpopulation.
#    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


BOARD_SIZE = 8
NOTHING = '.'


board = [[NOTHING] * BOARD_SIZE] * BOARD_SIZE  # indexing: (row, col)

for row in board:
    for c in row:
        print(c, end='')
    print()
