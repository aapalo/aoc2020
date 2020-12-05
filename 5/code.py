#!/usr/bin/python3

import time

'''     #######     '''

date = 5
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def splitrange(full, char):
    if char in "LF":
        # upper half
        return full[:int(len(full)/2)]
    else:
        # lower half
        return full[int(len(full)/2):]

def day(te):
    rows = list(range(128))
    cols = list(range(8))
    ids = set()
    for t in te:
        col = cols[:]
        row = rows[:]
        for c in t:
            if c in "FB":
                row = splitrange(row, c)
            else:
                col = splitrange(col, c)
        ids.append(row[0] * 8 + col[0])

    return max(ids)

def day2(te):
    rows = list(range(128))
    cols = list(range(8))
    ids = set()
    for t in te:
        col = cols[:]
        row = rows[:]
        for c in t:
            if c in "FB":
                row = splitrange(row, c)
            else:
                col = splitrange(col, c)
        ids.add(row[0] * 8 + col[0])

    for j in range(1, max(ids)-1):
        #ID is not in the list, but its neighbours are
        if j not in ids:
            if (j-1) in ids:
                if (j+1) in ids:
                    return(j)

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
