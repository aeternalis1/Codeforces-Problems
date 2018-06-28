import sys
raw_input = sys.stdin.readline
n = int(raw_input())
nums = list(map(int,raw_input().split()))
dp = [[0 for x in range(n)] for x in range(n)]
for i in range(n):
  dp[i][i] = nums[i]
for i in range(1,n):
  for j in range(n-i):
    dp[j][j+i] = dp[j][j+i-1]^dp[j+1][j+i]
for i in range(n-1,0,-1):
  for j in range(n-1,i-1,-1):
    dp[i-1][j] = max(dp[i-1][j],dp[i][j])
for i in range(n):
  for j in range(i+1,n):
    dp[i][j] = max(dp[i][j],dp[i][j-1])

q = int(raw_input())
for i in range(q):
  a,b = map(int,raw_input().split())
  print dp[a-1][b-1]
