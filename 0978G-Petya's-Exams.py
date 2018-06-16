n,m = map(int,raw_input().split())
exams = [-1 for x in range(n)]
ans = [-1 for x in range(n)]
for i in range(m):
  a,b,c = map(int,raw_input().split())
  a -= 1
  b -= 1
  ans[b] = m+1
  exams[b] = [a,c,i]
queue = []
valid = 1
for i in range(n-1,-1,-1):
  if exams[i] != -1:
    queue.append(exams[i])
    queue = sorted(queue,reverse=True)
    continue
  if not queue:
    ans[i] = 0
  else:
    if queue[0][0] > i:
      valid = 0
    ans[i] = queue[0][2]+1
    queue[0][1] -= 1
    if not queue[0][1]:
      queue.pop(0)
if not valid or queue:
  print -1
else:
  print " ".join([str(x) for x in ans])
