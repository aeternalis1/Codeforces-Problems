import sys
sys.setrecursionlimit(1000000)
n = int(raw_input())
names = []
taken = {}
for i in range(n):
  a,b = raw_input().split()
  names.append([a[:3],a[:2]+b[0]])
  taken[names[i][0]] = -1
  taken[names[i][1]] = -1
assi = ['' for x in range(n)]
sec = [0 for x in range(n)]
for i in range(n):
  for j in range(i+1,n):
    if names[i][0]==names[j][0]:
      sec[i] = 1
      sec[j] = 1
valid = 1
for i in range(n):
  if sec[i]:
    if taken[names[i][1]] != -1:
      valid = 0
    else:
      taken[names[i][1]] = i
      assi[i] = names[i][1]

checked = [0 for x in range(n)]

def dfs(cur):
  if checked[cur]:
    return 0
  checked[cur] = 1
  if sec[cur]:
    return 0
  if taken[names[cur][0]]==-1:
    taken[names[cur][0]] = cur
    assi[cur] = names[cur][0]
    return 1
  elif taken[names[cur][1]]==-1:
    taken[names[cur][1]] = cur
    assi[cur] = names[cur][1]
    return 1
  elif dfs(taken[names[cur][0]]):
    taken[names[cur][0]] = cur
    assi[cur] = names[cur][0]
    return 1
  elif dfs(taken[names[cur][1]]):
    taken[names[cur][1]] = cur
    assi[cur] = names[cur][1]
    return 1
  return 0

for i in range(n):
  if not sec[i]:
    checked = [0 for x in range(n)]
    if not dfs(i):
      valid = 0

if valid:
  print "YES"
  for i in assi:
    print i
else:
  print "NO"
