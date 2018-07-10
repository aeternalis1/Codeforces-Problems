from __future__ import division
from collections import deque
n = int(raw_input())
A = list(map(int,raw_input().split()))
B = list(map(int,raw_input().split()))
dp = [9999999999999999999 for x in range(n)]
dp[0] = 0
lines = deque()
lines.appendleft([B[0],0])

def solve(a,b):
  return (a[1]-b[1])/(b[0]-a[0])

for i in range(1,n):
  while len(lines)>=2 and solve(lines[-1],lines[-2]) <= A[i]:
    lines.pop()
  dp[i] = lines[-1][1]+lines[-1][0]*A[i]
  while len(lines)>=2 and solve(lines[1],lines[0]) >= solve(lines[0],[B[i],dp[i]]):
    lines.popleft()
  lines.appendleft([B[i],dp[i]])
print dp[n-1]
