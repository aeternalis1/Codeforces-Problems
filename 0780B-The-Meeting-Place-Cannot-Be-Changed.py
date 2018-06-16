from __future__ import division
N = int(raw_input())
nums = list(map(int,raw_input().split()))
nums2 = list(map(int,raw_input().split()))
lo = 0
hi = pow(10,9)
ans = 9999999999999
while (abs(lo-hi)>0.0000001):
  mid = (hi-lo)/3
  t1 = lo+mid
  t2 = hi-mid
  res1 = 0
  res2 = 0
  for i in range(N):
    res1 = max(res1,abs(nums[i]-t1)/nums2[i])
    res2 = max(res2,abs(nums[i]-t2)/nums2[i])
  if res1 > res2:
    lo = t1
  elif res1 < res2:
    hi = t2
  else:
    lo = t1
    hi = t2
  ans = min(res1,res2,ans)
print ans
