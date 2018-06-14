n = int(raw_input())
dp = [[0 for x in range(2001)] for x in range(n+1)]
track = [[[-1,-1] for x in range(2001)] for x in range(n+1)]
inds = [[-1 for x in range(2001)] for x in range(n+1)]
arr = []
for i in range(n):
  a,b,c = map(int,raw_input().split())
  arr.append([b,a,c,i])
arr = sorted(arr)
ans = 0
for i in range(1,n+1):
  b,a,c,ind = arr[i-1]
  for j in range(b-a-1,-1,-1):
    if dp[i-1][j]+c > dp[i][j+a]:
      dp[i][j+a] = dp[i-1][j]+c
      track[i][j+a] = [i-1,j]
      inds[i][j+a] = ind
      ans = max(ans,dp[i][j+a])
  for j in range(2001):
    if dp[i-1][j] > dp[i][j]:
      dp[i][j] = dp[i-1][j]
      track[i][j] = track[i-1][j]
      inds[i][j] = inds[i-1][j]
for i in range(2001):
  if dp[n][i]==ans:
    s = [n,i]
    break
arr = []
while track[s[0]][s[1]][1] != -1:
  arr.insert(0,inds[s[0]][s[1]]+1)
  s = track[s[0]][s[1]]
print ans
print len(arr)
print " ".join([str(x) for x in arr])
