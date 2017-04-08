import sys

def find(n):
  (l,m) = divmod(n, 2)
  if m == 0:
    if l > 1:
      res = [l, l-1]
    else:
      res = [l, 0]
  else:
    if l >= m:
      res = [l, l-m]
    if l == m:
      res = [l, m]
    if l < m:
      res = [l, 0]
  return res

def determine(l,r):
  if l > r :
    return l
  else:
    return r

def looparray(n, k):
  i = 0
  tmpl = n
  tmpr = 0
  a = [tmpl,tmpr]
  a.sort()
  
  while i < k:
    if len(a) > 0:
      no = a.pop()
      res = find(no)
      if res[0] > 0:
        a.append(res[0])
      if res[1] > 0:
        a.append(res[1])
      a.sort()
    else:
      res = [0,0]
      break
    i = i+1
  return res

name = "C-small-1-attempt4"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())

for t in xrange(T):
    line = f.readline().strip().split(' ')
    print line
    (n,k) = map(int, line)
    res = looparray(n, k)
    s = "Case #%d: %d %d\n" % (t+1, res[0] , res[1])
    print s
    o.write(s)
