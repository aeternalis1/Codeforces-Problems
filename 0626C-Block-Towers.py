n,m = map(int,raw_input().split())
sp = 0
for i in xrange(1,3000001):
  if i%3==0 and m:
    m -= 1
    if i%2==0:
      sp += 1
  elif i%3==0 and i%2 and i > 3 and sp:
    sp -= 1
    n -= 1
  elif i%2==0 and n:
    n -= 1
  if m==0 and n==0:
    ans = i
    break
print ans
