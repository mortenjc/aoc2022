#!/usr/local/bin/python3

import sys
#import defaultdict
from copy import deepcopy
#from collections import deque


def compare(l, r):
    #print(f'compare(): l {l}, r{r}')
    if type(l) is list and type(r) is list:
        done = False
        while (not done):
            if len(l) and len(r): # both have data
                a = l.pop(0)
                b = r.pop(0)
                compare(a, b)
            elif len(l) and not len(r):
                raise Exception("bad order")
            elif not(len(l)) and len(r):
                raise Exception("good order")
            else:
                done = True

    elif type(l) is int and type(r) is int:
        if l == r:
            return
        if l < r:
            raise Exception("good order")
        else:
            raise Exception("bad order")

    elif type(l) is list and type(r) is int:
        compare(l, [r])
    elif type(l) is int and type(r) is list:
        compare([l], r)
    else:
        assert False

def cmp(a, b):
    try:
        #print(f'compare {l} with {r}')
        compare(a, b)
    except Exception as inst:
        #print(inst.args)
        if inst.args[0] == 'good order':
            return True
        else:
            return False

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))
data = open(infile).read().strip()
#lines = [x for x in data.split('\n\n')]with open(ifile) as fin:

with open(infile) as fin:
        lines = ((fin.read().strip()).split('\n\n'))

# part 1
n = 0
for i, line in enumerate(lines):
    pair = i + 1
    l, r = line.replace('\n', ' ').split()
    l = eval(l)
    r = eval(r)
    if cmp(l, r):
        n += pair
S1 = n

#part 2
all = []
for line in lines:
    first, second = line.replace('\n', ' ').split()
    all.append(eval(first))
    all.append(eval(second))
all.append([[2]])
all.append([[6]])

for i in range(len(all)):
    for j in range(len(all)):
        if i == j:
            continue
        a = deepcopy(all[i])
        b = deepcopy(all[j])
        if cmp(a, b):
            tmp = all[i]
            all[i] = all[j]
            all[j] = tmp
da = 0
db = 0
for i, val in enumerate(all):
    if val == [[2]]:
        da = i + 1
    if val == [[6]]:
        db = i + 1
S2 = da*db


print("------------- A -------------")
print(f'S1 {S1}')
print("------------- B -------------")
print(f'S2 {S2}')
print("-----------------------------")
