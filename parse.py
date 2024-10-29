#!/usr/bin/env python


'''
Read a square region of alive cells.
'''


import re


EXAMPLE_FROM_PARAM = '(   4,999999),(7,  0)                   , (3,3)'
EXAMPLE_FROM_FILE = '''\
4, 999999
                     7,0

3             ,3
'''


# Exactly two nonegative integers separated by a comma.
XY = r'(\d+)\s*,\s*(\d+)'


def parse(p):
    for coord in p.split('(')[1:]:
        xy = re.search(XY, coord)
        x = xy.group(1)
        y = xy.group(2)
        print(x, y)


if __name__ == '__main__':
    parse(EXAMPLE_FROM_PARAM)
