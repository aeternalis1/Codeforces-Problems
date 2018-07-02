n,m = map(int,raw_input().split())
arr = []
for i in range(m):
  arr.append(list(map(int,raw_input().split())))
res = 0
ans = -1
for i in range(1,150):
  found = 1
  for j in range(m):
    if (arr[j][0]-1)/i!=arr[j][1]-1:
      found = 0
  if found:
    res += 1
    if ans==-1:
      ans = (n-1)/i+1
    elif ans != (n-1)/i+1:
      res = -9999

if res < 1:
  print -1
else:
  print ans
