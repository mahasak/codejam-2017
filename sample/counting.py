if 1:
    import sys



def reset_seen():
    dict = {}
    for i in range(0, 10):
        dict[i] = False
    return dict

def all_seen(dict):
    return all(value == True
        for value in dict.values())

def seen(dict, n):
    for c in str(n):
        dict[int(c)] = True
    return dict

def test_seen(dict):
    for i in range(0, 10):
        dict[i] = True
    return dict

def count(n):
    seen_dict = reset_seen()
    i = 1
    insomnia = True
    while (insomnia):
        if n == 0:
            return "INSOMNIA"
        tmp = n * i
        seen(seen_dict, tmp)
        if (all_seen(seen_dict)):
            return tmp
        else :
            i = i + 1

name = "A-large-practice"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())

print T
for t in xrange(T):
    l = int(f.readline())
    res = count(l)
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)