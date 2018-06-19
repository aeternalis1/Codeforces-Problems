n = int(raw_input())
ans = []
for i in range(n,max(n-100,-1),-1):
  cur = i
  for j in range(len(str(i))):
    cur += int(str(i)[j])
  if cur==n:
    ans.append(i)
print len(ans)
ans = sorted(ans)
for i in ans:
  print i
