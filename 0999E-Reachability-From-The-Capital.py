n,m,s = map(int,raw_input().split())
paths = [[] for x in range(n)]
paths2 = [[] for x in range(n)]
for i in range(m):
  a,b = map(int,raw_input().split())
  a -= 1
  b -= 1
  paths[a].append(b)
  paths2[b].append(a)

queue = [s-1]
checked = [0 for x in range(n)]
checked[s-1] = 1
while queue:
  c = queue.pop(0)
  for i in paths[c]:
    if not checked[i]:
      checked[i] = 1
      queue.append(i)

ans = 0

for j in range(n):
  if not checked[j] and not paths2[j]:
    checked[j] = 1
    ans += 1
    queue = [j]
    while queue:
      c = queue.pop(0)
      for i in paths[c]:
        if not checked[i]:
          checked[i] = 1
          queue.append(i)

for j in range(n):
  if not checked[j]:
    checked[j] = 1
    ans += 1
    queue = [j]
    while queue:
      c = queue.pop(0)
      for i in paths[c]:
        if not checked[i]:
          checked[i] = 1
          queue.append(i)

print ans
