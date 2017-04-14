#! /usr/bin/python

import sys

def sort_letter(l1, l2):
    if (ord(l1) > ord(l2)):
        return "%s%s" % (l1, l2)
    else:
        return "%s%s" % (l2,l1)

def solve(word):
    if len(word) == 1:
        return word
    return word_solve(sort_letter(word[0], word[1]), word[2:])

def word_solve(w1,w2):
    if len(w2) > 0:
        tmp = w2[0]
        if ord(tmp) >= ord(w1[0]):
            return word_solve(tmp + w1, w2[1:])
        else:
            return word_solve(w1 + tmp, w2[1:])
    return w1

name = "A-large-practice"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())
sys.setrecursionlimit(1500)

print T
for t in xrange(T):
    line = f.readline().strip()
    res = solve(line)
    s = "Case #%d: %s\n" % (t + 1, res)
    #print s
    o.write(s)


