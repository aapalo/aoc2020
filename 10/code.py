#!/usr/bin/python3

import time

'''     #######     '''

date = 10
dev = 0 # extra prints
part = 2 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def day(te):
    ones = 0
    threes = 1
    joltage = 0
    for t in sorted(te):
        if t == joltage + 1:
            ones += 1
        elif t == joltage + 2:
            pass
        elif t == joltage + 3:
            threes += 1
        else:
            print("difference > 3")
            break
        joltage = t
        #print(t)
    print(ones, threes)
    return ones * threes

def day2(te):
    biggest = max(te) + 3
    j = {}
    j[0] = 1
    for i in [1,2,3]:
        if i in te:
            j[i] = 1
    for t in sorted(te):
        for i in [1,2,3]:
            if (t+i) in te:
                try:
                    j[t+i] += j[t]
                except:
                    j[t+i] = j[t]
        if 0:
            print(sorted(te))
            print(j)
            print("---")
    return max(j.values())
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

t = [int((x.strip().replace('  ',' '))) for x in t]

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
