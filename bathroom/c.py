import sys

def bathroom(size):
  l = [0] * size
  l[0] = 1
  l[len(l)-1] = 1
  return l

def choose(l, size):
  indexes = [i for i,x in enumerate(l) if x == 0] 
  min_arr = [0] * size
  max_arr = [0] * size
  min_chosen = 0
  max_chosen = 0
  #print indexes
  for i in indexes:
    #print "determin index %d" % i
    d = determine(l,i)
    #print d
    min_arr[i] = d[0]
    max_arr[i] = d[1]
  #print "Min(L,R) : %s" % "".join(map(str,min_arr))
  #print "Max(L,R) : %s" % "".join(map(str,max_arr))
  cond1 = [x for x,item in enumerate(min_arr) if item==max(min_arr) and x !=0 and x!= size-1]
  cond2 = [0] * size
  if len(cond1) > 1:
    
    #print "more than one"
    #print cond1
    for x2 in cond1:
      cond2[x2] = max_arr[x2]
    max_cond = max(cond2)
    #print "Max cond 2 = %d" % max_cond
    cond3 = [x2 for x2,item in enumerate(max_arr) if item==max_cond and x2 !=0 and x2!= size-1]
    #print cond3
    idx = cond3[0]
    return [idx, [max_arr[idx], min_arr[idx]]]
  else:
    idx = cond1[0]
    return [idx, [max_arr[idx], min_arr[idx]]]

def determine(l,i):
  tmp = l[:]
  
  #print "\r\n"
  #print "Determine list %s at %d" % ("".join(map(str, l)), i)
  indexes = [j for j,x in enumerate(l) if x == 1] 
  #print indexes
  for k in range(0, len(indexes) - 1):
    if indexes[k] <= i <= indexes[k+1]:
      #print "Checking by range [%d -> %d ]" % (indexes[k], indexes[k+1])
      kk = l[indexes[k]:indexes[k+1]+1]
      #print kk
      
      idx = i - indexes[k]
      #print "i(%d) - k(%d) = (%d)" % (i, k , idx)
      #print idx
      kk[idx] = 1
      #print kk
      
      tmp_min = min(kk[:idx].count(0), kk[idx:].count(0)) #minls
      tmp_max = max(kk[:idx].count(0), kk[idx:].count(0)) #maxrs
      res = [tmp_min, tmp_max]
      #print res
      return res
  #print "-------------------------------------------"
  #print "\r\n"

def pick(l, i):
  l[i] = 1
  return l


def solve(n,k):
  size = n+2  

  b = bathroom(size)
  for i in range (0,k):
    print "round %d " %i
    res = choose(b,size)
    b = pick(b,res[0])
  print "===================================================="
  return res[1]


name = "C-small-1-attempt0"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())

print T
for t in xrange(T):
    line = f.readline().strip().split(' ')
    (n,k) = map(int, line)
    res = solve(n, k)
    s = "Case #%d: %s %s\n" % (t+1, res[0] , res[0])
    print s
    o.write(s)
