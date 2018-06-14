N = int(raw_input())
nums = list(map(int,raw_input().split()))
nums2 = list(map(int,raw_input().split()))
dp = [[99999999999 for x in range(3)] for x in range(N)]
for i in range(N):
  dp[i][0] = nums2[i]
  for j in range(i-1,-1,-1):
    for k in range(2):
      if dp[j][k] != 99999999999 and nums[j] < nums[i]:
        dp[i][k+1] = min(dp[i][k+1],dp[j][k]+nums2[i])

ans = 99999999999
for i in range(N):
  ans = min(dp[i][2],ans)
if ans==99999999999:
  print -1
else:
  print ans
