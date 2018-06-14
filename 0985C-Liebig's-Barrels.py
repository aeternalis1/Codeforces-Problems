import sys
from bisect import bisect_right
raw_input = sys.stdin.readline
n,k,l = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
nums = sorted(nums)
cur = nums[0]
taken = [cur]
ind = bisect_right(nums,cur+l)
extra = n*k-ind
cnt = 1
for i in range(ind-1,0,-1):
  if extra+cnt >= k:
    taken.append(nums[i])
    if extra > 0:
      extra -= k-cnt
    cnt = 0
  cnt += 1
if len(taken) < n:
  print 0
else:
  print sum(taken)
