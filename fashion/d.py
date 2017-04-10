import sys

name = "D-small-attempt0"
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
        print "".join(map(str,i))

def check_rule(g,i,j):
    max_row = len(g) - 1
    max_col = len(g[0]) - 1
    print max_col
    if g[i][j] == '.':
        print "col(%d,%d) , col(%d,%d) and col(%d,%d)" % (i,j, i+1, j, i, j+1)

        if ((i+1 <= max_row) and g[i+1][j] == '.') and ((j+1 <= max_col) and (g[i][j+1] == '.')):
            g[i][j] = 'O'

def has_left(g,i,j):
    max_row = len(g) - 1
    max_col = len(g[0]) - 1
    if j-1 > 0:
        return True
    else:
        return False

def has_right(g,i,j):
    max_row = len(g) - 1
    max_col = len(g[0]) - 1
    if j+1 < 0:
        return True
    else:
        return False

def has_upper(g,i,j):
    max_row = len(g) - 1
    max_col = len(g[0]) - 1
    if i-1 > 0:
        return True
    else:
        return False

def has_down(g,i,j):
    max_row = len(g) - 1
    max_col = len(g[0]) - 1
    if i+1 < max_row:
        return True
    else:
        return False

def check_row(r):
    res = False
    for i in range(0,n):
        if r[i] == '+':
            res = True

def solve(g,n):
    row = len(g)
    col = len(g[0])
    check = [[False]*n for i in range(n)]
    for i in range(0,row):
        for j in range(0,col):
            check_rule(g,i,j)
    print_grid(g)
            
for t in xrange(T):
    configs = f.readline().strip().split(' ')
    (n,m) = map(int, configs)
    print "%d x %d" % (n , n)
    # Prepare the board
    grid = create_grid(n)
    for r in range(0,m):
        line = f.readline().strip().split(' ')
        fill_model(grid, line)
    # Solve
    print_grid(grid)
    #solve(grid,n)
    #res = looparray(n, k)
    #s = "Case #%d: %d %d\n" % (t+1, res[0] , res[1])
    #print s
    #o.write(s)
