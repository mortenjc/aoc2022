#!/usr/local/bin/python3

import argparse
from collections import deque

def get_data(filename):
    return [line.rstrip() for line in open(filename, 'r')]


def different(chars):
    s = set()
    for c in chars:
        if s&set(c):
            return False
        else:
            s.add(c)
    return True


def solve(lines, n):
    for line in lines:
        i = 0
        for i in range(len(line) - n):
            if different(line[i:i+n]):
                print("end of marker {}".format(i + n))
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    print("<<{}>>".format(args.f))
    l = get_data(args.f)
    print("############## A ##############")
    solve(l,4)
    print("############## B ##############")
    solve(l,14)
    #print("###############################")
