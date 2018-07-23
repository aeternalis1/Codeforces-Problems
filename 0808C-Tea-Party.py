n,w = map(int,raw_input().split())
ans = [0 for x in range(n)]
nums = list(map(int,raw_input().split()))
inds = [x for x in range(n)]
nums,inds = zip(*sorted(zip(nums,inds)))
for i in range(n):
  ans[inds[i]] = nums[i]/2+nums[i]%2
  w -= nums[i]/2+nums[i]%2
for i in range(n-1,-1,-1):
  if ans[inds[i]]<nums[i] and w > 0:
    ans[inds[i]],w = ans[inds[i]]+min(w,nums[i]-ans[inds[i]]),w-min(w,nums[i]-ans[inds[i]])
if w < 0:
  print -1
else:
  print " ".join([str(x) for x in ans])
