#! /usr/bin/python

import sys


def solve(word):
    if len(word) == 1:
        return word
    return word_solve(sort_letter(word[0], word[1]), word[2:])


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


