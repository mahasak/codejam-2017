if 1:
    import sys

def all_happy(s):
  return all(value == "+" for value in s)
  
def more_sad(s):
  sum_sad = sum_happy = 0
  for i in range(0,len(s)):
    if s[i] == "-" :
      sum_sad = sum_sad +1
    else:
      sum_happy = sum_happy +1
  if sum_sad > sum_happy:
    return True
  else:
    return False
def reversed(c):
  if c == "+":
    return "-"
  else:
    return "+"

def flip(s,n):
  tmp = map(reversed , s[:n])
  return s[n:] + "".join(tmp)
  
def flip_top(s,n):
  tmp = map(reversed , s[:n])
  return"".join(tmp) +  s[n:]
  
def flipper(s):
  if all(value == "-" for value in s):
    return flip(s,len(s))
  if s[0] == "+":
    for i in range(0,len(s)):
      if(s[i] != s[i+1]):
        return flip_top(s,i+1)
  else:
    for i in range(0,len(s)):
      if(s[i] != s[i+1]):
        return flip(s,i+1)

def process(pancake):
  i = 0
  while not all_happy(pancake):
    pancake = flipper(pancake)
    i = i +1
  return i


name = "B-large-practice"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())

print T
for t in xrange(T):
    l = f.readline().strip()
    res = process(l)
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)