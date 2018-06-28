n = int(raw_input())
nums = list(map(int,raw_input().split()))
dp = [0 for x in range(n)]
combs = [[0 for x in range(1001)] for x in range(1001)]
for i in range(1001):
  for j in range(i+1):
    if not j:
      combs[i][j] = 1
    elif j:
      combs[i][j] = (combs[i-1][j]+combs[i-1][j-1])%998244353
for i in range(n-1,-1,-1):
  if nums[i] > 0 and nums[i]+i<n:
    dp[i] = combs[n-i-1][nums[i]]%998244353
    for j in range(nums[i]+i+1,n):
      dp[i] = dp[i]+(dp[j]*combs[j-i-1][nums[i]])%998244353
print sum(dp)%998244353
