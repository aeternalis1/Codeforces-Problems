n,m = map(int,raw_input().split())
nums = []
on = [0 for x in range(m)]
for i in range(n):
  nums.append(list(raw_input()))
  for j in range(m):
    if nums[i][j]=='1':
      on[j] += 1
ans = False
for i in range(n):
  found = False
  for j in range(m):
    if nums[i][j]=='1' and on[j]==1:
      found = True
  if not found:
    ans = True
    break
if ans:
  print "YES"
else:
  print "NO"
