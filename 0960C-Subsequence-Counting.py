X,d = map(int,raw_input().split())
arr = []
while X > 0:
  cur = 1
  cnt = 0
  while cur-1 <= X:
    cur *= 2
    cnt += 1
  if cur-1 == X:
    arr.append(cnt)
    X -= cur-1
  else:
    arr.append(cnt-1)
    X -= cur/2-1
if len(arr)*(d+1) > pow(10,18)-1:
  print -1
else:
  n = sum(arr)
  out = []
  cur = 1
  for i in range(len(arr)):
    for j in range(arr[i]):
      out.append(cur)
    cur += d+1
  print n
  print " ".join([str(x) for x in out])
