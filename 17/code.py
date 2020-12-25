#!/usr/bin/python3

import time
#import copy
from collections import defaultdict
'''     #######     '''

date = 17 #11
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''
def countseats(d):
    return sum(d.values())

def printseats(dict):
    ylist = list(range(min(dict.keys()), max(dict.keys())))
    xlist = list(range(min(dict[0].keys()), max(dict[0].keys())))
    for j in dict.keys():
        row = str(j) + " "
        for k in dict[j].keys():
            try:
                row += dict[j][k]
            except:
                #print(j,k, dict[j][k])
                pass
        print(row)
    return 0

def comparedics(d1, d2):
    for i in d1.keys():
        for j in d1[i].keys():
            for k in d1[i][j].keys():
                if d1[i][j][k] != d2[i][j][k]:
                    return 0
    return 1

def countNeighbors(z, y, x, dict):
    neighbors = 0
    for d in [-1,0,1]:
        for r in [-1,0,1]:
            for c in [-1,0,1]:
                if [d,r,c] == [0,0,0]:
                    continue
                try:
                    if dict[(d+z),(r+y),(c+x)] == 1:
                        neighbors += 1
                except:
                    continue
    return neighbors

def cycle(d):
    n = {} #new dict
    # z, y, x,
    zlims = [min(k[0] for k in d.keys()), max(k[0] for k in d.keys())]
    ylims = [min(k[1] for k in d.keys()), max(k[1] for k in d.keys())]
    xlims = [min(k[2] for k in d.keys()), max(k[2] for k in d.keys())]
    for z in range(zlims[0]-1, 2+zlims[1]):
        for y in range(ylims[0]-1, 2+ylims[1]):
            for x in range(xlims[0]-1, 2+xlims[1]):
                cn = countNeighbors(z, y, x, d)
                try:
                    cube = d[(z,y,x)]
                except KeyError:
                    cube = 0
                if cube == 1:
                    if cn in [2,3]:
                        n[(z,y,x)] = 1
                    else:
                        n[(z,y,x)] = 0
                else:
                    if cn == 3:
                        n[(z,y,x)] = 1
                    else:
                        n[(z,y,x)] = 0
    return n

def day(te):
    seats = defaultdict(dict)
    x, y, z = 0, 0, 0
    for t in te:
        #print(t)
        x = 0
        for i in range(len(t)):
            if t[i] == "#":
                seats[(z,y,x)] = 1
            else:
                seats[(z,y,x)] = 0
            x += 1
        y += 1

    for c in range(6):
        seats = cycle(seats)

    return countseats(seats)

'''            ############        '''

def countNeighbors2(w, z, y, x, dict):
    neighbors = 0
    for t in [-1,0,1]:
        for d in [-1,0,1]:
            for r in [-1,0,1]:
                for c in [-1,0,1]:
                    if [t,d,r,c] == [0,0,0,0]:
                        continue
                    try:
                        neighbors += dict[(t+w),(d+z),(r+y),(c+x)]
                    except:
                        continue
    return neighbors

def cycle2(d):
    n = {} #new dict
    # w, z, y, x, get min and max for each
    wlims = [min(k[0] for k in d.keys()), max(k[0] for k in d.keys())]
    zlims = [min(k[1] for k in d.keys()), max(k[1] for k in d.keys())]
    ylims = [min(k[2] for k in d.keys()), max(k[2] for k in d.keys())]
    xlims = [min(k[3] for k in d.keys()), max(k[3] for k in d.keys())]
    for w in range(wlims[0]-1, 2+wlims[1]):
        for z in range(zlims[0]-1, 2+zlims[1]):
            for y in range(ylims[0]-1, 2+ylims[1]):
                for x in range(xlims[0]-1, 2+xlims[1]):
                    cn = countNeighbors2(w, z, y, x, d)
                    try:
                        cube = d[(w,z,y,x)]
                    except KeyError:
                        cube = 0
                    if cube == 1:
                        if cn in [2,3]:
                            n[(w,z,y,x)] = 1
                        else:
                            n[(w,z,y,x)] = 0
                    else:
                        if cn == 3:
                            n[(w,z,y,x)] = 1
                        else:
                            n[(w,z,y,x)] = 0
    return n

def day2(te):
    seats = defaultdict(dict)
    #seats[0] = defaultdict(dict)
    w, x, y, z = 0, 0, 0, 0
    for t in te:
        #print(t)
        x = 0
        for i in range(len(t)):
            if t[i] == "#":
                seats[(w,z,y,x)] = 1
            else:
                seats[(w,z,y,x)] = 0
            x += 1
        y += 1

    for c in range(6):
        seats = cycle2(seats)
    return sum(seats.values())
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
