N,M,K = map(int,raw_input().split())
arr = [0 for x in range(N)]
cnt = [0 for x in range(N)]
sz = [1 for x in range(N)]
par = [x for x in range(N)]
ran = [0 for x in range(N)]
if K > 1:
    nums = list(map(int,raw_input().split()))
else:
    nums = [int(raw_input())]
for i in nums:
    arr[i-1] = 1

def p(a):
    if a==par[a]:
        return a
    return p(par[a])

def merge(a,b):
    if ran[a]>ran[b]:
        par[b] = a
        cnt[a] += cnt[b]
        sz[a] += sz[b]
    elif ran[a]<ran[b]:
        par[a] = b
        cnt[b] += cnt[a]
        sz[b] += sz[a]
    else:
        ran[a] += 1
        par[b] = a
        sz[a] += sz[b]
        cnt[a] += cnt[b]

for i in range(M):
    a,b = map(int,raw_input().split())
    a -= 1
    b -= 1
    a1 = p(a)
    b1 = p(b)
    if a1==b1:
        cnt[a1] += 1
        continue
    cnt[a1] += 1
    if arr[a1] or arr[b1]:
        arr[a1] = 1
        arr[b1] = 1
    merge(a1,b1)

nums = []
nums2 = []
ans = 0

for i in range(N):
    if i==par[i]:
        ans += (sz[i]*(sz[i]-1))/2-cnt[i]
        if arr[i]:
            nums.append([sz[i],i])
        else:
            nums2.append([sz[i],i])

nums = sorted(nums,reverse=True)
nums2 = sorted(nums2,reverse=True)

for i in nums2:
    ans += i[0]*nums[0][0]
    nums[0][0] += i[0]
print ans
