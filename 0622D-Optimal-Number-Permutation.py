import sys
n = int(raw_input())
taken = [0 for x in range(n*2)]
got = [0 for x in range(n+1)]
taken[0] = n-1
taken[1] = n-1
cur = 1
if n==3:
  print 1,3,1,2,2,3
  sys.exit()
for i in range(n/2):
  taken[i] = cur
  taken[i+n-cur] = cur
  cur += 2
cur = 2
for i in range(n,n+n/2):
  taken[i] = cur
  taken[i+n-cur] = cur
  cur += 2
  if cur==n:
    break
for i in range(n*2):
  if not taken[i]:
    taken[i] = n

print " ".join([str(x) for x in taken])
