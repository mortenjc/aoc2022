#!/usr/local/bin/python3

import sys
import re
from collections import defaultdict

D1 = ['D1', [( 0,-1), ( 1,-1), (-1,-1)], ( 0,-1)] # N, NE, NW
D2 = ['D2', [( 0, 1), ( 1, 1), (-1, 1)], ( 0, 1)] # S, SE, SW
D3 = ['D3', [(-1, 0), (-1,-1), (-1, 1)], (-1, 0)] # W, NW, SW
D4 = ['D4', [( 1, 0), ( 1,-1), ( 1, 1)], ( 1, 0)] # E, NE, SE
DS = [D1, D2, D3, D4]


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


def getlimits(p):
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    for e in p:
        xmin = min(xmin, e[0])
        xmax = max(xmax, e[0])
        ymin = min(ymin, e[1])
        ymax = max(ymax, e[1])
    return [xmin, xmax, ymin, ymax]


def draw(p):
    count = 0
    lim = getlimits(p)
    for r in range(lim[2], lim[3]+1):
        line = ''
        for c in range(lim[0], lim[1]+1):
            if (c,r) in p:
                line += '#'
            else:
                count+=1
                line +='.'
        print(f'{r:<3} {line}')
    return count


P = set()
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '#':
            P.add((c, r))
        else:
            assert ch == '.'

print(f'start limits: {getlimits(P)}')

N = len(P)

# D1 no Elf in the N, NE, or NW adjacent positions,  moving north one step.
# D2 no Elf in the S, SE, or SW adjacent positions,  moving south one step.
# D3 no Elf in the W, NW, or SW adjacent positions,  moving west one step.
# D4 no Elf in the E, NE, or SE adjacent positions,  moving east one step.
def getmove(p, DS):
    A8 = [(0,-1), (0,1), (1,0), (-1,0), (1,-1), (1,1), (-1,1), (-1,-1)]
    x = p[0]
    y = p[1]

    if not any([x in P for x in [(x+z[0], y+z[1]) for z in A8]]):
        #print(f'no neigbours, no action ({x},{y})')
        return (x, y), 1

    found = False
    hit=''
    for D in DS:
        #print(D[0],D[1], D[2])
        if not any([x in P for x in [(x+z[0], y+z[1]) for z in D[1]]]):
            hit = D[0]
            found = True
            nx = x + D[2][0]
            ny = y + D[2][1]
            break
    if found != True:
        nx = x
        ny = y
    #print(f'move proposal {x},{y} -> {nx},{ny} ({hit})')
    return (nx, ny), 0


def move(P, DS):
    notmoved = 0
    M = defaultdict(lambda: 0)
    assert len(M) == 0
    for e in P:
        m, nm = getmove(e, DS)
        M[m]+= 1

    newP = set()

    for i, e in enumerate(P):
        m, nm = getmove(e, DS)
        notmoved += nm
        assert M[m] != 0
        if (M[m] > 1):
            #print(f'{i}: {e} -> {m} would collide {M[m]}, stay put')
            mc = e
        else:
            #print(f'{i}: {e} -> {m}')
            mc = m
        assert not mc in newP, mc
        newP.add(mc)
    #print(f'P    {P}')
    #print(f'newP {newP}')
    assert len(P) == len(newP)
    return newP, notmoved

draw(P)
nmvs = 0
i = 1
while nmvs != N:
    print(f'round {i}')
    P, nmvs = move(P, DS)
    DS = DS[1:] + DS[:1]
    c = draw(P)
    if i == 10:
        S1 = c
    i+=1

S2 = 0
print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
