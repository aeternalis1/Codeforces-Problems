n,l,r = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
nums2 = list(map(int,raw_input().split()))
inds = [x for x in range(n)]
nums2,nums,inds = zip(*sorted(zip(nums2,nums,inds)))
val = [0 for x in range(n)]
val[inds[0]] = l-nums[0]
ans = [0 for x in range(n)]
ans[inds[0]] = l
valid = 1
for i in range(1,n):
  tar = val[inds[i-1]]+1
  if tar+nums[i] < l:
    val[inds[i]] = l-nums[i]
    ans[inds[i]] = l
  elif tar+nums[i] > r:
    valid = 0
  else:
    val[inds[i]] = tar
    ans[inds[i]] = tar+nums[i]
if not valid:
  print -1
else:
  print " ".join([str(x) for x in ans])
