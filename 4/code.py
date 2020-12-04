#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 4
dev = 0 # extra prints
part = 2 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def dprint(i):
    if dev:
        for j in i:
            print(i)
    return 0

def isPresent(passport):
    fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"] # "cid:"
    #print(passport)
    for f in fields:
        if f not in passport:
            #print(f, "missing")
            return 0
    return 1

def day(te):
    line = ""
    ans = 0
    for t in te:
        if t == "":
            ans += isPresent(line)
            #print("check: ", ans, line)
            line = ""
        else:
            line += t
            #print(ans, line)
    ans += isPresent(line)
    #print("check: ", ans, line)
    return ans

def isValid(field):
    f = (field.split(":"))
    if f[0] == "byr":
        try:
            if (1920 <= int(f[1])) and (int(f[1]) <= 2002):
                return 1
            else:
                return 0
        except:
            return 0
    elif f[0] == "iyr":
        try:
            if (2010 <= int(f[1])) and (int(f[1]) <= 2020):
                return 1
            else:
                return 0
        except:
            return 0
    elif f[0] == "eyr":
        try:
            if (2020 <= int(f[1])) and (int(f[1]) <= 2030):
                return 1
            else:
                return 0
        except:
            return 0
    elif f[0] == "hgt":
        if not (("cm" in f[1]) or ("in" in f[1])):
            return 0
        unit = f[1][-2:]
        try:
            height = int(f[1][:-2])
        except:
            return 0
        if unit == "cm":
            if (150 <= height) and (height <= 193):
                return 1
        elif unit == "in":
            if (59 <= height) and (height <= 76):
                return 1
        else:
            return 0
    elif f[0] == "hcl":
        if (f[1][0] == "#") and (len(f[1]) == 7):
            return 1
        else:
            return 0
    elif f[0] == "ecl":
        if f[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return 1
        else:
            return 0
    elif f[0] == "pid":
        if len(f[1]) == 9:
            try:
                if int(f[1]) > 0:
                    return 1
            except:
                return 0
    elif f[0] == "cid":
        return 1

    return 0

def day2(te):
    line = ""
    passports = []
    ans = 0
    for t in te:
        if t == "":
            passports.append(line)
            line = ""
        else:
            line += " " + t
    notOK = 0
    for p in passports:
        if isPresent(p) == 0:
            continue
        for i in p.split():
            if isValid(i) == 0:
                notOK = 1
                dprint("not valid")
                break
        if notOK == 0:
            ans += 1
        else:
            notOK = 0


    #print("check: ", ans, line)
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
        #t = f.read()
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
