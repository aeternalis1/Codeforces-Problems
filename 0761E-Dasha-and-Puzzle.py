import sys
n = int(raw_input())
paths = [[] for x in range(n)]
for i in range(n-1):
  a,b = map(int,raw_input().split())
  a -= 1
  b -= 1
  paths[a].append(b)
  paths[b].append(a)

pts = [[0,0] for x in range(n)]

for i in range(n):
  if len(paths[i])>4:
    print "NO"
    sys.exit()

moves = [[0,1],[-1,0],[1,0],[0,-1]]
moves2 = [[0,-1],[1,0],[-1,0],[0,1]]

def solve(cur,par,x,y,dist,last):
  pts[cur] = [x,y]
  cnt = 0
  for i in range(len(paths[cur])):
    if paths[cur][i]==par:
      continue
    if moves[cnt]==last:
      cnt += 1
    solve(paths[cur][i],cur,x+moves2[cnt][0]*dist/2,y+moves2[cnt][1]*dist/2,dist/2,moves2[cnt])
    cnt += 1

solve(0,-1,0,0,1<<40,-1)

print "YES"
for i in pts:
  print i[0],i[1]
