#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 9
dev = 0 # extra prints
part = 2 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def checksum(nrs, result):
    if samp:
        preamble = 5
    else:
        preamble = 25
    for i in range(preamble):
        for j in range(preamble):
            if i == j:
                continue
            if nrs[i] == nrs[j]:
                continue
            #print(" ", i, j, nrs[i], nrs[j], nrs[i] + nrs[j])
            if (nrs[i] + nrs[j]) == result:
                if samp:
                    print("found: ", nrs[i], nrs[j],  result)
                return 1
    #print("not found", result, nrs[-preamble:])
    return 0

def day(te):
    numbers = []
    numset = set()
    if samp:
        preamble = 5
    else:
        preamble = 25
    for t in te:
        if len(numbers) > preamble:
            if checksum(numbers[-preamble:], t) == 0:
                return t
        numbers.append(t)
        #numset.add(t)
        #print(numbers)
    return 0

def contiguous(nrs, ans):
    s = 0
    n = []
    for i in range(len(nrs)):
        s += nrs[i]
        n.append(nrs[i])
        if s > ans:
            return 0
        if (s == ans):
            r = min(n) + max(n)
            return r
    return 0


def day2(te):
    if samp:
        ans = 127
    else:
        ans = 1398413738
    numbers = []
    for t in te:
        if t >= ans:
            break
        numbers.append(t)
    # reverse the list
    numbers = numbers[::-1]
    for t in range(len(numbers)):
        r = contiguous(numbers[t:], ans)
        if r != 0:
            return r

    return 0

'''     #######     '''

time0 = time.time()

if samp == 1:
    filename = "/sample.txt"
else:
    filename = "/input.txt"

try:
    with open(str(date) + filename,"r") as f:
        t = f.readlines()
except FileNotFoundError:
    with open("." + filename,"r") as f:
        t = f.readlines()

t = [(int(x.strip().replace('  ',' '))) for x in t]

if part == 1:
    print("Part 1: ", day(t))
elif part == 2:
    print("Part 2: ", day2(t))
elif part == 3:
    #run both
    print("Part 1: ", day(t))
    print("Part 2: ", day2(t))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
