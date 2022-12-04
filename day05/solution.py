#!/usr/local/bin/python3

import argparse

def get_data(filename):
    lines = [line.rstrip() for line in open(filename, 'r')]
    print("get_data - read {} lines".format(len(lines)))
    return lines


# def one_is_covered(a, b):
#     return (a&b == b) or (a&b == a)


# def regions_overlap(a, b):
#     return a&b


# def make_range(rangestr):
#     a = rangestr.split('-')[0]
#     b = rangestr.split('-')[1]
#     l = list(range(int(a), int(b)+1))
#     return l

# def make_sets(line):
#     regions = line.split(",")
#     rb = set(make_range(regions[0]))
#     ra = set(make_range(regions[1]))
#     return ra, rb


def solve(lines):
    for line in lines:
        print(line)
    return

def solve2(lines):
    for line in lines:
        print(line)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    l = get_data(args.f)
    print("############## A ##############")
    solve(l)
    print("############## B ##############")
    solve2(l)
