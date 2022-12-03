#!/usr/local/bin/python3

import argparse


def get_data(filename):
    INPUT = open(filename, "r")
    lines = INPUT.readlines()
    print("get_data - read {} lines".format(len(lines)))
    return lines


def solve(lines):
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    l = get_data(args.f)
    solve(l)
