import sys

name = "D-practice"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())

def create_grid(n):
    #return [['.'] * n] * n
    return [['.']*n for i in range(n)]

def fill_model(g, d):
    row = int(d[1]) - 1
    col = int(d[2]) - 1
    #print "put %s, row %d, col %d" % ( d[0], row + 1, col + 1)
    #print g[row]
    g[row][col] = d[0]

def print_grid(g):
    for i in g:
        print "".join(i)

def check_rule(g,n):
    for r in range(0,n):
        check_row(g[r])

def check_row(r):
    res = False
    for i in range(0,n):
        if r[i] == '+':
            res = True
            
for t in xrange(T):
    configs = f.readline().strip().split(' ')
    (n,m) = map(int, configs)
    print "%d x %d" % (n , n)
    grid = create_grid(n)
    for r in range(0,m):
        line = f.readline().strip().split(' ')
        fill_model(grid, line)
    print_grid(grid)
    check_rule(grid,n)
    #res = looparray(n, k)
    #s = "Case #%d: %d %d\n" % (t+1, res[0] , res[1])
    #print s
    #o.write(s)
