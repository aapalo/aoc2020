#!/usr/bin/python3

import time

'''     #######     '''

date = 25
dev = 0 # extra prints
part = 1 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''
def transform(val, sn):
    val = val * sn
    val = val % 20201227
    return val

def day(te):
    for t in te:
        print(t)
    loopsize = [0,0]
    val = 1
    i = 0
    while 1:
        val = transform(val, 7)
        if val == te[0]:
            loopsize[0] = i + 1
            print("Ls0", loopsize[0])
            break
        if val == te[1]:
            loopsize[1] = i + 1
            print("Ls1", loopsize[1])
            break
        i += 1
    #print(loopsize)
    ans = 1
    if loopsize[0] > 0:
        for j in range(loopsize[0]):
            ans = transform(ans, te[1])
    elif loopsize[1] > 0:
        for j in range(loopsize[1]):
            ans = transform(ans, te[0])
    return ans

def day2(te):

    return 0

'''     #######     '''

time0 = time.time()

if samp == 1:
    t = (5764801, 17807724)
else:
    t = (11239946, 10464955)

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
