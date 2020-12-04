#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 3
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''


def day(te):
    rows = len(te)
    cols = len(te[0])
    trees = 0
    r = 0
    c = 0
    for t in te:
        if (t[c] == "#"):
            trees += 1
        c = (c+3) % cols
        r += 1
        #print(trees, r, c)
    return trees

def day2(te):
    rows = len(te)
    cols = len(te[0])
    treecount = []
    slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]] #[r,c]
    for s in slopes:
        r = 0
        c = 0
        trees = 0
        dr = s[0]
        dc = s[1]
        while r < rows:
            if (te[r][c] == "#"):
                trees += 1
            c = (c + dc) % cols
            r += dr
        treecount.append(trees)
        #print(s, trees)
    ans = 1
    for i in treecount:
        ans = ans*i
    return ans

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

t = [(x.strip().replace('  ',' ')) for x in t]

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
