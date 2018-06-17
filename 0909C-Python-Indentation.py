n = int(raw_input())
dp = [[0 for x in range(n)] for x in range(n)]
dp[0][0] = 1
last = raw_input()
for i in range(1,n):
  cur = raw_input()
  if cur=='f' and last=='f':
    for j in range(n-1):
      dp[i][j+1] = dp[i-1][j]%1000000007
  elif cur=='f':
    res = 0
    for j in range(i-1,-1,-1):
      res = (res+dp[i-1][j])%1000000007
      dp[i][j] = res%1000000007
  elif cur=='s' and last=='f':
    for j in range(n-1):
      dp[i][j+1] = dp[i-1][j]%1000000007
  else:
    res = 0
    for j in range(i-1,-1,-1):
      res = (res+dp[i-1][j])%1000000007
      dp[i][j] = res%1000000007
  last = cur
print sum(dp[n-1])%1000000007
