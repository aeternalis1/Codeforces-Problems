q = int(raw_input())
for i in range(q):
  a = int(raw_input())
  if a <= 3:
    print -1
    continue
  b = a/4
  c = a%4
  d = 0
  e = 0
  if c==1:
    b -= 2
    d += 1
  if c==2:
    b -= 1
    e += 1
  if c==3:
    b -= 3
    e += 1
    d += 1
  if b < 0:
    print -1
  else:
    print b+e+d

#use 4,6,9
