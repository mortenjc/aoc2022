#!/usr/local/bin/python3

import argparse
from collections import deque

def get_data(filename):
    lines = [line.rstrip() for line in open(filename, 'r')]
    print("get_data - read {} lines".format(len(lines)))
    return lines


def solve(lines):
    for line in lines:
        print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    l = get_data(args.f)
    print("############## A ##############")
    solve(l)
    print("############## B ##############")
    solve(l)
    #print("###############################")
