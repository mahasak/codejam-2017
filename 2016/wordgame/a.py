#! /usr/bin/python

import sys

def sort_letter(l1, l2):
    if (ord(l1) > ord(l2)):
        s = "%s%s" % (l1, l2)
        #print s
        return s
    else:
        s = "%s%s" % (l2,l1)
        #print s
        return s

def solve(word):
    if len(word) == 1:
        return word
    print "%s , %s " % (word[:2], word[2:] )
    return word_solve(sort_letter(word[0], word[1]), word[2:])

def solve_large(word):
    if len(word) == 1:
        return word
    print "%s , %s " % (word[:2], word[2:] )
    tmp = sort_letter(word[0], word[1])
    end = len(word)
    n = 2
    while(n < end):
        if ord(word[n]) >= ord(tmp[0]):
            print word[n] + tmp
            print "case 1"
            tmp = word[n] + tmp
        else:
            print "case 2"
            print tmp + word[n]
            tmp = tmp + word[n]
    #return word_solve(sort_letter(word[0], word[1]), word[2:])


def word_solve(w1,w2):
    if len(w2) > 0:
        tmp = w2[0]
        if ord(tmp) >= ord(w1[0]):
            print tmp + w1
            print "case 1"
            print "%s , %s " % (w1 + tmp, w2[1:] )
            return word_solve(tmp + w1, w2[1:])
        else:
            print "case 2"
            print w1 + tmp
            print "%s , %s " % (w1 + tmp, w2[1:] )
            return word_solve(w1 + tmp, w2[1:])
    return w1

name = "A-large-practice"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())
#print solve("CODE")
print T
for t in xrange(T):
    line = f.readline().strip()
    res = solve_large(line)
    s = "Case #%d: %s\n" % (t + 1, res)
    print s
    o.write(s)


