#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 12
dev = 0 # extra prints
part = 2 # 1,2, or 3 for both
samp = 1 # 0 or 1

'''     #######     '''

def turn(d, nd, deg):
    mul = (1) if (nd == "L") else (-1)
    d = (d + mul*(deg/90))%4
    return int(d)

# direction, steps
def move(d, s):
    # E, N, W, S
    if d == 1:
        return [s, 0]
    elif d == 2:
        return [0, s]
    elif d == 3:
        return [-s, 0]
    elif d == 0:
        return [0, -s]
    return [0,0]

def day(te):
    dir = 1 # [0,1,2,3] # direction: N,E,S,W
    stepdir = 0
    x = 0
    y = 0
    for t in te:
        d = t[0]
        steps = int(t[1:])
        #print(d, steps)
        [dx, dy] = [0, 0]
        if d in ["L","R"]:
            dir = turn(dir, d, steps)
            continue
            #[dx, dy] = move(dir, steps)
        elif d == "N":
            dy = steps
        elif d == "E":
            dx = steps
        elif d == "S":
            dy = -steps
        elif d == "W":
            dx = -steps
        elif d == "F":
            [dx, dy] = move(dir, steps)
        [x,y] = [x+dx, y+dy]
        #print([x,y], dir)
    return (abs(x)+abs(y))

def turnwp(wpx, wpy, deg):


def day2(te):
    [wpx, wpy] = [10,1] # waypoint coords from ship
    [x, y] = [0,0] # ship coords
    dir = 1
    for t in te:
        d = t[0]
        steps = int(t[1:])
        #print(d, steps)

        [dx, dy] = [0, 0]
        if d in ["L","R"]:
            dir = turn(dir, d, steps)
            continue
        elif d == "N":
            wpy += steps
        elif d == "E":
            wpx += steps
        elif d == "S":
            wpy -= steps
        elif d == "W":
            wpx -= steps
    return (abs(x)+abs(y))

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
