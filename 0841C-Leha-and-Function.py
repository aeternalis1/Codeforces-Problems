n = int(raw_input())
nums = list(map(int,raw_input().split()))
nums2 = list(map(int,raw_input().split()))
inds = [x for x in range(n)]
nums2,inds = map(list,zip(*sorted(zip(nums2,inds))))
nums = sorted(nums,reverse=True)
ans = [0 for x in range(n)]
for i in range(n):
  ans[inds[i]] = nums[i]
print " ".join([str(x) for x in ans])
