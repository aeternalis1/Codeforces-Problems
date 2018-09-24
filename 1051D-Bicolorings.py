N,K = map(int,raw_input().split())
dp = [[[0 for x in range(4)] for x in range(K+2)] for x in range(N)]
dp[0][1][0] = 1
dp[0][2][1] = 1
dp[0][2][2] = 1
dp[0][1][3] = 1
mod = 998244353
for i in range(1,N):
    for j in range(4):
        for k in range(4):
            cur = j^k
            if j==k:
                for l in range(K+1):
                    if dp[i-1][l][j]:
                        dp[i][l][k] += dp[i-1][l][j]
                        dp[i][l][k] %= mod
            elif cur&1 and cur&2 and bool(j&1)!=bool(j&2):
                for l in range(K):
                    if dp[i-1][l][j]:
                        dp[i][l+2][k] += dp[i-1][l][j]
                        dp[i][l+2][k] %= mod
            elif cur&1 and cur&2:
                for l in range(K+1):
                    if dp[i-1][l][j]:
                        dp[i][l+1][k] += dp[i-1][l][j]
                        dp[i][l+1][k] %= mod
            elif bool(j&1)==bool(j&2):
                for l in range(K+1):
                    if dp[i-1][l][j]:
                        dp[i][l+1][k] += dp[i-1][l][j]
                        dp[i][l+1][k] %= mod
            elif bool(k&1)==bool(k&2):
                for l in range(K+1):
                    if dp[i-1][l][j]:
                        dp[i][l][k] += dp[i-1][l][j]
                        dp[i][l][k] %= mod
ans = 0
for i in range(4):
    ans += dp[N-1][K][i]
    ans %= mod
print ans
