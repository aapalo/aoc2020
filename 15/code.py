#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

date = 15
dev = 0 # extra prints
part = 1 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''


def day(te):
    d = {} #when a number was spoken
    ans = [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]
    spoken = None

    for i in range(30000000):#2020):
        if i < (len(te)):
            # starting numbers:
            number = te[i]
        else:
            if spoken in d:
                number = i - d[spoken]
            else:
                number = 0

        d[spoken] = i
        if samp and i <= 10:
            print(i, spoken, ans[i-1])
        i += 1
        spoken = number
    return spoken

def day2(te):

    return 0

'''     #######     '''

time0 = time.time()

if samp:
    t = [2,3,1]
else:
    t = [9,6,0,10,18,2,1]


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
