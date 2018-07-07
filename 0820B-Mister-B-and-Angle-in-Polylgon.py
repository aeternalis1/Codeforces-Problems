from __future__ import division
n,A = map(int,raw_input().split())
a = 1
b = 2
c = 3
ans = abs(A-(180-360/n))
res = 3
cur = 180-360/n
for i in range(3,n):
  cur -= cur/(n-i+1)
  if abs(A-cur) < ans:
    ans = abs(A-cur)
    res = i+1
print a,b,res
