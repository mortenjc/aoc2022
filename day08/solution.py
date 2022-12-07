#!/usr/local/bin/python3

import argparse
import sys
#from collections import deque
#from collections import defaultdict
import copy


def solve(lines):
    for line in lines:
        pass


def solve2(lines):
    for line in lines:
        pass



if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(ifile))

    lines = [line.rstrip() for line in open(ifile, 'r')]
    print("############## A ##############")
    solve(lines)
    print("############## B ##############")
    solve2(lines)
    print("###############################")
