#!/usr/local/bin/python3

import argparse

def get_data(filename):
    lines = [line.rstrip() for line in open(filename, 'r')]
    print("get_data() - read {} lines".format(len(lines)))
    return lines


def one_is_covered(a, b):
    return (a&b == b) or (a&b == a)


def regions_overlap(a, b):
    return a&b


def make_range(rangestr):
    a = int(rangestr.split('-')[0])
    b = int(rangestr.split('-')[1])
    return list(range(a, b + 1))


def make_sets(line):
    regions = line.split(",")
    rb = set(make_range(regions[0]))
    ra = set(make_range(regions[1]))
    return ra, rb


def solve(lines):
    covered = 0
    for line in lines:
        a, b = make_sets(line)
        if one_is_covered(a, b):
            covered = covered + 1
    print("{} are covered".format(covered))
    return

def solve2(lines):
    overlaps = 0
    for line in lines:
        a, b = make_sets(line)
        if regions_overlap(a, b):
            overlaps = overlaps + 1
    print("{} assignments overlap".format(overlaps))
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
    print("###############################")
