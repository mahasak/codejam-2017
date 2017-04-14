#! /usr/bin/python

import sys

name = "B-large-practice"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())
sys.setrecursionlimit(1500)

print T
for t in xrange(T):
    size = int(f.readline())

    all = []
    for i in range((size*2)-1):
        all += map(int, f.readline().strip().split(" "))
    
    line = []
    for i in set(all):
        if(all.count(i)%2):
            line.append(i)
            
    res = " ".join(map(str, sorted(line)))
    s = "Case #%d: %s\n" % (t + 1, res)
    print s
    o.write(s)

