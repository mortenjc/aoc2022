#!/usr/local/bin/python3

import sys
#import defaultdict
from copy import deepcopy
import math
import networkx as nx
from matplotlib import pyplot as plt


def getmoves(graph, G, x, y, S, E):
    #print(f'getmoves ({x},{y})')
    f = f'({x},{y})'
    if (x, y) == S:
        #print(f'visited S')
        val = ord('a')
    elif (x, y) == E:
        #print(f'visited E')
        val = ord('z')
    else:
        val = ord(G[y][x])

    moves = [(max(x-1, 0), y), (min(x+1, len(G[0])-1), y),
    (x, max(y-1, 0)), (x, min(y+1, len(G)-1))  ]
    moves = [i for i in moves if i != (x,y)]

    #print(f'all valid {moves}')

    for m in moves:
        t = f'({m[0]},{m[1]})'
        cc = G[m[1]][m[0]]
        nextval = ord(cc)

        if nextval == val:
            print(f'= val {val}({chr(val)}), nextval {nextval}({chr(nextval)})')
            print(f'= valid {f} <-> {t}   {chr(val)}<->{chr(nextval)}')
            graph.add_edge(f, t)
            graph.add_edge(t, f)
        elif nextval == val +1:
            print(f'> val {val}({chr(val)}), nextval {nextval}({chr(nextval)})')
            print(f'> valid {f}  -> {t}   {chr(val)} ->{chr(nextval)}')
            graph.add_edge(f, t)
        elif nextval < val:
            # print(f'< val {val}, nextval {nextval}')
            # print(f'< valid {t} -> {f}   {chr(nextval)}->{chr(val)}')
            # graph.add_edge(t, f)
            pass
        else:
            print(f'invalid val {val}, nextval {nextval}')
            print(f'invalid f{f} -> t{t}   {chr(val)}->{chr(nextval)}')



infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

G = deepcopy(lines)
S = ''
E = ''
for r in range(len(G)):
    for c in range(len(G[r])):
        if ord(G[r][c]) == ord('S'):
            S = (c, r)
        if ord(G[r][c]) == ord('E'):
            E = (c, r)

print(S, E)

graph = nx.MultiDiGraph()
for r in range(len(G)):
    for c in range(len(G[0])):
        getmoves(graph, G, c, r, S, E)


# plt.tight_layout()
# graph2 = nx.DiGraph()
# graph2.add_edges_from(
#     [('A', 'B'), ('A', 'C'), ('C', 'A'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
#      ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])
# nx.draw_networkx(graph2, arrows=True)
# # nx.draw_networkx(graph, arrows=True)
# plt.savefig("g1.png", format="PNG")
# plt.show()
# plt.clf()

print(graph.nodes())

Ss = f'({S[0]},{S[1]})'
Es = f'({E[0]},{E[1]})'
print(Ss, Es)
sp = nx.shortest_path(graph, Ss, Es)
print(sp)
print(len(sp))






print("------------- A -------------")
#print('S1', S[0])
print("------------- B -------------")
#print('S2', S[1])
print("-----------------------------")
