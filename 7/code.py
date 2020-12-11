#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 7
dev = 0 # extra prints
part = 2 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def day(te):
    colors = []
    goldbags = []
    bags = {}
    # vibrant bronze bags contain 1 faded maroon bag, 4 plaid indigo bags, 2 bright purple bags, 5 dim violet bags.
    maxlen = 0
    for t in te:
        b = []
        idx = 0
        t = t.split()
        #print(t)
        printer = 0
        bagdaddy = t[idx] + "-" +t[idx+1]
        if bagdaddy not in colors:
            colors.append(bagdaddy)
        if bagdaddy not in bags:
            bags[bagdaddy] = []
        idx += 5
        while idx < (len(t) -1 ):
            bagname = t[idx] + "-" +t[idx+1]
            bags[bagdaddy].append(bagname)
            idx += 4

    golds = 0
    for c in colors:
        if "shiny-gold" in bags[c]:
            goldbags.append(c)
    #print(goldbags)
    for i in range(3):
        for g in goldbags:
            for c in colors:
                if g in bags[c]:
                    if c not in goldbags:
                        goldbags.append(c)
        #print(len(goldbags), goldbags)

    #print(colors)
    #print(bags)
    return len(goldbags)

def bagsInABag(b, bags):
    bcount = 0
    for [bag, mult] in bags[b]:
        bcount += mult
        bcount += mult * bagsInABag(bag, bags)
        #print(bcount, bag, bags[b])
    return bcount

def day2(te):
    colors = []
    goldbags = []
    bags = {}
    maxlen = 0
    for t in te:
        b = []
        idx = 0
        t = t.split()
        printer = 0
        bagdaddy = t[idx] + "-" + t[idx+1]
        if bagdaddy not in colors:
            colors.append(bagdaddy)
        if bagdaddy not in bags:
            bags[bagdaddy] = []
        idx += 5
        while idx < (len(t) -1 ):
            bagname = t[idx] + "-" +t[idx+1]
            if t[idx-1] != "no":
                bags[bagdaddy].append([bagname, int(t[idx-1])])
            else:
                pass
                #bags[bagdaddy] = 0
            idx += 4
    if 0:
        for b in bags.keys():
            print(b, ":", bags[b])
    print(bagsInABag("shiny-gold", bags))
    return len(goldbags)

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
