#!/usr/bin/python3

import time
import copy
'''     #######     '''

date = 11
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def countAdjacent(r, c, dict):
    adj = 0
    rmax = len(dict.keys())
    cmax = len(dict[0])
    for y in [-1,0,1]:
        if ((r+y) > rmax) or ((r+y) < 0):
            continue
        for x in [-1,0,1]:
            if ((c+x) > cmax) or ((c+x) < 0):
                continue
            if [x,y] == [0,0]:
                continue
            try:
                if dict[r+y][c+x] == "#":
                    adj += 1
                    # save time:
                    if adj >= 4:
                        return adj
            except:
                continue
            #print(r,c,dict[r+y][c+x],adj)
    return adj

def countseats(dict):
    s = 0
    for i in dict.values():
        s += i.count("#")
    return s

def printseats(dict):
    for i in dict.values():
        row = ""
        for j in i:
            row += j
        print(row)
    return 0

def comparedics(d1, d2):
    for k in d1.keys():
        if d1[k] != d2[k]:
            return 0
    return 1

def day(te):
    seats = {}
    x, y = 0, 0
    for t in te:
        seats[y] = list(t)
        y += 1

    cols = len(seats[0])
    c = 0
    while 1:
        newseats = copy.deepcopy(seats)
        for y in seats.keys():
            for x in range(cols):
                #print(y, x, seats[y][x], countAdjacent(y, x, seats))
                if seats[y][x] == ".":
                    continue
                if seats[y][x] == "L":
                    if countAdjacent(y, x, seats) == 0:
                        newseats[y][x] = "#"
                elif seats[y][x] == "#":
                    if countAdjacent(y, x, seats) >= 4:
                        newseats[y][x] = "L"

        #print(c, countseats(seats))
        #printseats(newseats)
        c += 1
        if c > 20 and comparedics(newseats, seats):
            if samp:
                printseats(newseats)
            return countseats(seats)
        else:
            seats = copy.deepcopy(newseats)

        if c > 10000:
            break


    return 0

def visadjacent(r, c, dict):
    adj = 0
    dirs = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1, -1]]
    rows = 1
    for d in dirs:
        i = 1
        while 1:
            # save time:
            if adj == 5:
                return adj
            x = c + d[1]*i
            y = r + d[0]*i
            xmax = len(dict[0])
            ymax = len(dict.keys())
            if (y > ymax) or (y < 0):
                break
            if (x > xmax) or (x < 0):
                break
            try:
                if dict[y][x] == "#":
                    adj += 1
                    break
                elif dict[y][x] == "L":
                    break
                elif dict[y][x] == ".":
                    i += 1
                    continue
            except:
                pass
            i += 1
        #print(d, adj)
    return adj

def day2(te):
    seats = {}
    x, y = 0, 0
    for t in te:
        seats[y] = list(t)
        y += 1

    cols = len(seats[0])
    c = 0
    while 1:
        newseats = copy.deepcopy(seats)
        for y in seats.keys():
            for x in range(cols):
                #print(y, x, seats[y][x], countAdjacent(y, x, seats))
                if seats[y][x] == ".":
                    continue
                if seats[y][x] == "L":
                    if visadjacent(y, x, seats) == 0:
                        newseats[y][x] = "#"
                elif seats[y][x] == "#":
                    if visadjacent(y, x, seats) >= 5:
                        newseats[y][x] = "L"

        #print(c, countseats(seats))
        #printseats(newseats)
        c += 1
        if c > 10 and comparedics(newseats, seats):
            if samp:
                printseats(newseats)
            return countseats(seats)
        else:
            seats = copy.deepcopy(newseats)

        if c > 30000:
            print("took too long")
            break
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
