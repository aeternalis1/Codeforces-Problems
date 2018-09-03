import sys
raw_input = sys.stdin.readline
N,M,K = map(int,raw_input().split())
X,S = map(int,raw_input().split())
arr1 = [list(map(int,raw_input().split())) for x in range(2)]
arr2 = [list(map(int,raw_input().split())) for x in range(2)]
ans = N*X
ind = K-1
for i in range(K):
    if arr2[1][i]<=S:
        ans = min(ans,(N-arr2[0][i])*X)
for i in range(M):
    if arr1[1][i]<=S:
        ans = min(ans,N*arr1[0][i])
for i in range(M):
    lo = 0
    hi = K-1
    t = S-arr1[1][i]
    if t<0:
        continue
    while lo<=hi:
        mid = (lo+hi)/2
        if arr2[1][mid]<=t:
            lo = mid+1
        else:
            hi = mid-1
    lo -= 1
    if arr2[1][lo]<=t:
        ans = min(ans,(N-arr2[0][lo])*arr1[0][i])
print ans
