# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 07:47:41 2018

@author: Chen
"""
import sys
def NWDistance(seedSequence, candidateSequence):
    s = -1  # a mismatch would deduce 1 point.
    m = 1  # plus 1 point for one match.
    g = -2  # deduce 2 point for one gap.
    seedSequence = seedSequence.strip()
    candidateSequence = candidateSequence.strip()
    if len(seedSequence) == 0:
        print ("Error, seed sequence length equal zero.")
        sys.exit(1)
    elif len(candidateSequence) == 0:
        print ("Error, candidate sequence length equal zero.")
        sys.exit(1)
    sLen = len(seedSequence)
    cLen = len(candidateSequence)
    table = []
    for o in range(0, len(seedSequence) + 1):
        table.append([o * g])
    table[0] = []
    for n in range(0, len(candidateSequence) + 1):
        table[0].append(n * g)
    for i in range(sLen):
        for j in range(cLen):
            table[i + 1].append(
                max(
                    table[i][j] + (m if seedSequence[i] == candidateSequence[j] else s),
                    table[i][j + 1] + g,
                    table[i + 1][j] + g,
                )
            )
    print(table)
    i = sLen-1
    j = cLen-1
    #print (j)
   # print(seedSequence[0],candidateSequence[j])
    NewSeed = seedSequence[i]
    NewCandidate = candidateSequence[j]
    print(NewSeed,NewCandidate)
    if len(seedSequence) <= 1 or len(candidateSequence) <= 1:
        print ("Error, too short!")
        sys.exit(1)
    while True:
        if i ==0 and j ==0:
            break
        if seedSequence[i] == candidateSequence[j]:
            if table[i - 1][j - 1] + 1 > table[i - 1][j] - 2 and table[i - 1][j - 1] + 1 > table[i][j - 1] - 2:
                i = i - 1
                j = j - 1
                NewSeed = u"%s%s" % (seedSequence[i], NewSeed)
                NewCandidate = u"%s%s" % (candidateSequence[j], NewCandidate)
                #i=i-1
                #j=j-1
                print(1)
            else:
                if table[i][j + 1] > table[i + 1][j]:#######################
                    i = i - 1
                    NewSeed = u"%s%s" % (seedSequence[i], NewSeed)
                    NewCandidate = u"%s%s" % ('-', NewCandidate)
                    print(2)
                else:
                    j = j - 1
                    NewSeed = u"%s%s" % ('-', NewSeed)
                    NewCandidate = u"%s%s" % (candidateSequence[j], NewCandidate)
                    print(3)
        else:
            if table[i - 1][j - 1] + 1 > table[i - 1][j] - 2 and table[i - 1][j - 1] + 1 > table[i][j - 1] - 2:
                i = i - 1
                j = j - 1
                NewSeed = u"%s%s" % (seedSequence[i], NewSeed)
                NewCandidate = u"%s%s" % (candidateSequence[j], NewCandidate)
                print(4)
            else:
                if table[i][j + 1] > table[i + 1][j]:#####################################
                    i = i - 1
                    NewSeed = u"%s%s" % (seedSequence[i], NewSeed)
                    NewCandidate = u"%s%s" % ('-', NewCandidate)
                    print(5)
                    #i=i-1
                else:
                    j = j - 1
                    NewSeed = u"%s%s" % ('-', NewSeed)
                    NewCandidate = u"%s%s" % (candidateSequence[j], NewCandidate)
                    print(6)
                    #j=j-1
                    #print(NewSeed,NewCandidate)
    print (NewSeed)
    print (NewCandidate)
    # distance
    mismath = 0
    math = 0
    gap = 0
    charZipList = list(zip(NewSeed, NewCandidate))
    # delete the head gap
    for n in range(len(charZipList)):
        if "-" in charZipList[n]:
            del charZipList[0]
           # print (charZipList)
        else:
            break
    # delete the tail gap
    while True:
        lastTuple = charZipList.pop()
        #print (lastTuple)
        #print (charZipList)
        if "-" in lastTuple:
            #print (lastTuple)
            continue
        else:
            charZipList.append(lastTuple)
            break
    #print (charZipList)
    for n in range(len(charZipList)):
        charTuple = charZipList[n]
        if charTuple[0] == charTuple[1]:
            math += 1
        elif "-" in charTuple:
            gapLoc = charTuple.index("-")
            if charZipList[n + 1][gapLoc] == "-":
                #print(1111111)
                continue
            else:
                gap += 1
        else:
            mismath += 1
    distance = round(1.0 - float(math) / float(mismath + math + gap), 4)
    return distance