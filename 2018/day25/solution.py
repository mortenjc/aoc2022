#!/usr/local/bin/python3

import argparse, sys



def solve(grid):
    visible = best = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if isvisible(grid, c, r):
                visible += 1
            best = max(viewdist(grid, c, r), best)


def base(conn, i):
    while True:
        if conn[i] == i:
            print('base ', i)
            return i
        else:
            i = conn[i]
            print('iteration ', i)


if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(ifile))

    #lines = [line for line in open(ifile).read().splitlines()]
    lines = [line for line in open(ifile)]
    input = []
    for line in lines:
        input.append([eval(x) for x in line.strip().split(',')])
    lines = input

    # solve
    used = [False] * len(lines)
    conn = [-1] * len(lines)

    for i in range(len(lines)):
        print("# {}".format(i))
        for j in range(len(lines)):
            if i > j:
                print("({},{}) skip".format(i,j))
                continue

            md = sum([abs(lines[i][x] - lines[j][x]) for x in range(len(lines[i]))])
            if md == 3:
                print("({},{}) md 3".format(i,j))
                print(used[i], used[j])
                b1 = base(conn, i)
                b2 = base(conn, j)
                
                if used[i]:
                    conn[j] = base(conn, i)
                else:
                    conn[j] = i
                print(conn)
                used[j] = True
                used[i] = True
            elif md == 0: # duplicate or self
                if i == j:
                    print("({},{}) md 0 self".format(i,j))
                    print(used[i], used[j])
                    if used[i]:
                        conn[j] = base(conn, j)
                    else:
                        conn[j] = j
                    print(conn)
                    used[j] = True
                else:
                    print("({},{}) md 0 duplicate".format(i,j))
                    print(used[i], used[j])
                    assert 1 == 0
                    #conn[j] = i
                    #used[j] = True
            else:
                print("({},{}) - ".format(i,j))


    print(conn)

    print("------------- A -------------")
    #print("visible {}".format(visible))
    #print("------------- B -------------")
    #print("best    {}".format(best))
    print("-----------------------------")
