from __future__ import division
from bisect import bisect_left
import sys
raw_input = sys.stdin.readline
n,U = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
ans = 0
for i in range(n-2):
  a = nums[i]
  b = nums[i+1]
  c = bisect_left(nums,a+U)
  if c==n:
    c -= 1
  if nums[c] > a+U:
    c -= 1
  if c>i+1:
    ans = max(ans,(nums[c]-b)/(nums[c]-a))
if ans==0:
  print -1
else:
  print ans
