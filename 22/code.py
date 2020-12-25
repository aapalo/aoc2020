#!/usr/bin/python3

import time

'''     #######     '''

date = 22
dev = 0 # extra prints
part = 3 # 1,2, or 3 for both
samp = 0 # 0 or 1

'''     #######     '''

def countscore(cards):
    sum = 0
    i = len(cards)
    j = 0
    while i > 0:
        sum += cards[j] * i
        i -= 1
        j += 1
    return sum

def game(one, two):
    playedgames = set()
    while 1:
        gamestr = str(one)+str(two)
        if gamestr in playedgames:
            return (1,0)
        else:
            playedgames.add(gamestr)
        o = one.pop(0)
        t = two.pop(0)
        if o > t:
            one.append(o)
            one.append(t)
        else:
            two.append(t)
            two.append(o)
        if 0:
            print(one, two)
        if min(len(one),len(two)) == 0:
            break
    if samp:
        print("1:", countscore(one))
        print("2:", countscore(two))
    return (countscore(one),countscore(two))


def day(te):
    one = []
    two = []
    isone = 1
    for t in te:
        if t == "":
            isone = 0
            continue
        try:
            if isone:
                one.append(int(t))
            else:
                two.append(int(t))
        except:
            continue
    #print(one, two)
    return max(game(one,two))

def day2(te):
    one = []
    two = []
    isone = 1
    playedgames = set()
    for t in te:
        if t == "":
            isone = 0
            continue
        try:
            if isone:
                one.append(int(t))
            else:
                two.append(int(t))
        except:
            continue

    scores = [0,0]
    while 1:
        if samp:
            print(one, "\t\t\t", two)
        gamestr = str(one)+str(two)
        if gamestr in playedgames:
            print("Round already played. Player 1 wins.")
            return scores[0]
            #continue
        else:
            playedgames.add(gamestr)
        o = one.pop(0)
        t = two.pop(0)
        if (len(one) < o) or (len(two) < t):
            if o < t:
                two.append(t)
                two.append(o)
                scores[1] += 1
            else:
                one.append(o)
                one.append(t)
                scores[0] += 1
        else:
            ocopy = one[:o].copy()
            tcopy = two[:t].copy()
            results = game(ocopy,tcopy)
            if results[0] < results[1]:
                two.append(t)
                two.append(o)
                scores[1] += 1
            else:
                one.append(o)
                one.append(t)
                scores[0] += 1
        if min(len(one),len(two)) == 0:
            break
    #print(one, two)
    #print(scores)
    return max((countscore(one),countscore(two)))

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
