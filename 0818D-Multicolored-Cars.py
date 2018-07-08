n,A = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
occ = [[] for x in xrange(1000001)]
for i in range(n):
  occ[nums[i]].append(i)
cur = len(occ[A])
val = 0
for i in xrange(1,1000001):
  if occ[i] and i != A and len(occ[i])>=cur:
    val = 1
    for j in range(cur):
      if occ[i][j] > occ[A][j]:
        val = 0
        break
    if val:
      print i
      break
if not val:
  print -1
