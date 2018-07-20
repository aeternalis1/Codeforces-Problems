n,k,p = map(int,raw_input().split())
nums = sorted(list(map(int,raw_input().split())))
nums2 = sorted(list(map(int,raw_input().split())))
ans = 99999999999
for i in range(k-n+1):
  res = 0
  for j in range(n):
    res = max(res,abs(nums[j]-nums2[i+j])+abs(nums2[i+j]-p))
  ans = min(ans,res)
print ans
