from copy import deepcopy
import sys
raw_input = sys.stdin.readline
n,m = map(int,raw_input().split())
grid = []
rows = [[] for x in range(n)]
cols = [[] for x in range(m)]
checked = [0 for x in range(n)]
checked2 = [0 for x in range(m)]
for i in range(n):
  grid.append(list(raw_input().strip('\n')))
  for j in range(m):
    if grid[i][j]=='#':
      rows[i].append(j)
      cols[j].append(i)
found = False
for i in range(n):
  if not checked[i] and rows[i]:
    queue = deepcopy(rows[i])
    cs = deepcopy(rows[i])
    rs = []
    while queue:
      for j in range(len(queue)):
        c = queue.pop(0)
        for k in cols[c]:
          if k not in rs:
            checked[k] = True
            rs.append(k)
            queue.append(k)
      for j in range(len(queue)):
        c = queue.pop(0)
        for k in rows[c]:
          if k not in cs:
            cs.append(k)
            queue.append(k)
    for j in rs:
      for k in cs:
        if grid[j][k] != '#':
          found = True
if found:
  print "No"
else:
  print "Yes"
