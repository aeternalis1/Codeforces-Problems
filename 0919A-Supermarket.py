from __future__ import division
n,m = map(int,raw_input().split())
ans = 9999999999
for i in range(n):
  a,b = map(int,raw_input().split())
  ans = min(ans,m/b*a)
print ans
