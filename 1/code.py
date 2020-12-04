#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 1
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''


def day(te):
    i = 0
    j = 0
    listlen = len(te)
    while i < listlen:
        while j < listlen:
            if i != j:
                if te[i] + te[j] == 2020:
                    return (te[i] * te[j])
            j += 1
        i += 1
        j = 0

    print(te)
    return 0

def day2(te):
    i = 0
    listlen = len(te)
    while i < listlen:
        j = 0
        while j < listlen:
            k = 0
            while k < listlen:
                if (i != j) and (j != k) and (i != k):
                    if te[i] + te[j] + te[k] == 2020:
                        print(te[i], te[j], te[k])
                        return (te[i] * te[j] * te[k])
                k += 1
            j += 1
        i += 1

    print(te)
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
t = [int(x) for x in t] #str to int

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
