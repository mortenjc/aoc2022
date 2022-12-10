#!/usr/local/bin/python3

import argparse, sys
#import defaultdict


if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(ifile))

    lines = [line.rstrip() for line in open(ifile, 'r')]
    #grid = [list( map(int, line)) for line in open(ifile).read().splitlines()]
    #print(grid)

    #G = [[' ' for _ in range(40)] for _ in range(6)]

    for line in lines:
        print(line)


    print("------------- A -------------")
    print('S1')
    print("------------- B -------------")
    print('S2')
    print("-----------------------------")
