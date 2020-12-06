#!/usr/bin/python3

from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 6
dev = 0 # extra prints
part = 2 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def day(te):
    a = []
    line = ""
    for t in te:
        if t == "":
            a.append(line)
            line = ""
        else:
            line += t
    ans = 0
    for t in a:
        ans += len(Counter(t))
        #print(ans, t)
    return ans

def allyes(q, m):
    #print(m, q)
    j = 0
    c = Counter(q)
    for k in c.keys():
        # if as many "yes" as group members, add 1
        if c[k] == m:
            j += 1
    return j

def day2(te):
    a = [] #answers
    gm = [] #group member count
    line = ""
    i = 0
    for t in te:
        if t == "":
            a.append(line)
            line = ""
            gm.append(i)
            i = 0
        else:
            line += t
            i += 1
    ans = 0
    for i in range(len(a)):
        ans += allyes(a[i], gm[i])
        #print(ans, t)
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
