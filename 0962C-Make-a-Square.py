n = list(raw_input())
N = len(n)
ans = 99
for i in range(1,1<<N):
  temp = []
  res = 0
  for j in range(N):
    if i&(1<<j):
      temp.append(n[j])
    else:
      res += 1
  if temp[0]=='0':
    continue
  cur = 0
  for j in range(len(temp)):
    cur *= 10
    cur += int(temp[j])
  if pow(int(pow(cur,0.5)),2)==cur:
    ans = min(ans,res)
if ans==99:
  print -1
else:
  print ans
