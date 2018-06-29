n,m,s,t = map(int,raw_input().split())
paths = [[] for x in range(n)]
con = [[0 for x in range(n)] for x in range(n)]
for i in range(m):
  a,b = map(int,raw_input().split())
  a -= 1
  b -= 1
  paths[a].append(b)
  paths[b].append(a)
  con[a][b] = 1
  con[b][a] = 1
s -= 1
t -= 1
q = [s]
checked = [0 for x in range(n)]
checked[s] = 1
while q:
  c = q.pop(0)
  for i in paths[c]:
    if not checked[i]:
      checked[i] = checked[c]+1
      q.append(i)
q = [t]
checked2 = [0 for x in range(n)]
checked2[t] = 1
while q:
  c = q.pop(0)
  for i in paths[c]:
    if not checked2[i]:
      checked2[i] = checked2[c]+1
      q.append(i)
checked = [x-1 for x in checked]
checked2 = [x-1 for x in checked2]
ans = 0
for i in range(n):
  for j in range(i+1,n):
    if not con[i][j]:
      if min(checked2[j]+checked[i]+1,checked2[i]+checked[j]+1) >= checked[t]:
        ans += 1
print ans
