n,m = map(int,raw_input().split())
nums = [x-1 for x in list(map(int,raw_input().split()))]
taken = [0 for x in range(n)]
ans = [-1 for x in range(n)]
val = 1
for i in range(m-1):
  if ans[nums[i]] != (nums[i+1]-nums[i])%n:
    if ans[nums[i]]==-1 and not taken[(nums[i+1]-nums[i])%n]:
      ans[nums[i]] = (nums[i+1]-nums[i])%n
      taken[(nums[i+1]-nums[i])%n] = 1
    else:
      val = 0
if not val:
  print -1
else:
  for i in range(n):
    if ans[i]==-1:
      for j in range(n):
        if not taken[j]:
          ans[i] = j
          taken[j] = 1
          break
    if ans[i]==0:
      ans[i] = n
  print " ".join([str(x) for x in ans])
