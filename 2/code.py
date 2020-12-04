#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 2
dev = 0 # extra prints
part = 1 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def count(c, word):
    j = 0
    for i in word:
        if i == c:
            j += 1
    return j

def day(te):
    valid = 0
    for t in te:
        t = (t.replace('-',' ').replace(':','').split())
        #print(t)
        low = int(t[0])
        high = int(t[1])
        char = t[2]
        word = t[3]
        times = count(char, word)
        if (low <= times) and (times <= high):
            valid += 1
    return valid

def day2(te):
    valid = 0
    for t in te:
        t = (t.replace('-',' ').replace(':','').split())
        #print(t)
        low = int(t[0]) - 1
        high = int(t[1]) - 1
        char = t[2]
        word = t[3]
        times = 0
        #times = count(char, word)
        if word[low] == char:
            times += 1
        if word[high] == char:
            times += 1
        if times == 1:
            valid += 1
    return valid

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
