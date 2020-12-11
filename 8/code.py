#!/usr/bin/python3

import time

'''     #######     '''

date = 8
dev = 0 # extra prints
part = 2 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def loop(te):
    acc = 0
    visited = set()
    i = 0
    finished = 0
    while 1:
        if i > (len(te) - 1):
            finished = 1
            break
        if i in visited:
            break
        else:
            visited.add(i)
        t = te[i].split()
        if t[0] == "acc":
            acc += int(t[1])
            i += 1
        elif t[0] == "jmp":
            if int(t[1]) == 0:
                break
            else:
                i += int(t[1])
        else:
            # "nop"
            i += 1
    return [acc, finished]

def day(te):
    return loop(te)[0]

def day2(te):
    for i in range(len(te)):
        tecopy = te[:]
        instr = tecopy[i].split()[0]
        val = tecopy[i].split()[1]
        if instr == "nop":
            tecopy[i] = "jmp " + val
        elif instr == "jmp":
            tecopy[i] = "nop " + val
        ans = loop(tecopy)
        if samp:
            print(i, tecopy[i], ans)
        if ans[1] == 1:
            print("Finished succesfully:", i)
            return ans[0]

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
