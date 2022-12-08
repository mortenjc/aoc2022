#!/usr/local/bin/python3

import argparse
import sys
#from collections import deque
#from collections import defaultdict
import copy
import pprint


def isvisible(board, x, y, n):
    #print("#{} {}".format(x,y))
    h = board[y][x]
    # visible from left
    sl = board[y][:x]
    if sum([1 for x in sl if x < h]) == len(sl):
        return True
    # visible from right
    sr = board[y][-(n - 1 -x):]
    if sum([1 for x in sr if x < h]) == len(sr):
        return True
    # visible from top
    #print("#top ({}, {})".format(x, y))
    st = [board[i][x] for i in range(n)]
    if sum([1 for x in st[:y] if x < h]) == len(st[:y]):
        return True
    # visible from bottom
    #print("#bottom ({}, {})".format(x, y))
    st = [board[i][x] for i in range(n)]
    if sum([1 for x in st[-(n - 1 -y):] if x < h]) == len(st[-(n - 1-y):]):
        return True

    return False

def viewdist(board, x, y, n):
    h = board[y][x]
    #print("# viewdist for ({},{}) - val {}".format(x, y, h))
    #left
    dl = 0
    dr = 0
    dt = 0
    db = 0
    for i in range(x - 1, -1, -1):
        #print("l i {} testing ({}, {}) val {}".format(i, i, y, board[y][i]))
        if (board[y][i] < h):
            dl += 1
        if (board[y][i] >= h):
            dl += 1
            break
    for i in range(x + 1, n):
        #print("r i {} testing ({}, {}) val {}".format(i, i, y, board[y][i]))
        if (board[y][i] < h):
            dr += 1
        if (board[y][i] >= h):
            dr += 1
            break

    for i in range(y - 1, -1, -1):
        #print("t testing ({}, {}) val {}".format(x, i, board[i][x]))
        if (board[i][x] < h):
            dt += 1
        if (board[i][x] >= h):
            dt += 1
            break

    for i in range(y+1, n):
        #print("b testing ({}, {}) val {}".format(x, i, board[i][x]))
        if (board[i][x] < h):
            db += 1
        if (board[i][x] >= h):
            db += 1
            break

    #print("({},{}) - {} {} {} {}".format(x, y, dl, dr, dt, db))
    return dl * dr * dt * db

def solve(lines):
    ny = len(lines)
    nx = len(lines[0])
    grid = []
    print(nx, ny)
    for line in lines:
        a = list(line)
        grid.append(a)
    #print(grid)

    visible = 0
    for y in range(1, ny - 1):
        for x in range(1, nx - 1):
            if isvisible(grid, x, y, nx):
                visible += 1
    visible += 4 * (nx - 1)
    print("visible {}".format(visible))


def solve2(lines):
    ny = len(lines)
    nx = len(lines[0])
    grid = []
    #print(nx, ny)
    for line in lines:
        a = list(line)
        grid.append(a)
    #print(grid)

    bs = 0
    for y in range(1, ny - 1):
        for x in range(1, nx - 1):
            s = viewdist(grid, x, y, nx)
            if s > bs:
                bs = s
                print("Best ({},{} - {})".format(x, y, bs))

    print("best {}".format(bs))




if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(ifile))

    lines = [line.rstrip() for line in open(ifile, 'r')]
    print("############## A ##############")
    solve(lines)
    print("############## B ##############")
    solve2(lines)
    print("###############################")
