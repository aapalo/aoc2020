#!/usr/bin/python3

import time

'''     #######     '''

date = 13
dev = 0 # extra prints
part = 2 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def day(te):
    earliest = int(te[0])
    buses = []
    for b in te[1].split(","):
        try:
            busnumber = int(b)
            buses.append(busnumber)
        except:
            pass
    t = earliest
    while 1:
        for b in buses:
            if (t % b) == 0:
                return (b*(t-earliest))
        t += 1
    # What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
    return 0

def day2(te):
    buses = []
    offset = 0
    for b in te[1].split(","):
        try:
            busnumber = int(b)
            buses.append([busnumber, offset])
        except:
            pass
        offset += 1
    #print(buses)
    dt = buses[0][0]
    t = buses[0][1]
    for number, offset in buses[1:]:
        while (t + offset) % number > 0:
            t += dt
        #print(number, dt, t)
        dt = dt * number
    return t

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
