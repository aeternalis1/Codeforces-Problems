import sys
n = int(raw_input())
ans = [1000000000000 for x in range(n)]
cnt = 1
for i in range(20):
    q = [0 for x in range(n)]
    arr = []
    cur = 0
    for j in range(n):
        if j%cnt==0:
            cur ^= 1
        q[j] = cur
        if cur:
            arr.append(j+1)
    if len(arr)==n or len(arr)==0:
        break
    print len(arr)
    sys.stdout.flush()
    print " ".join(map(str,arr))
    sys.stdout.flush()
    arr = list(map(int,raw_input().split()))
    for j in range(n):
        if q[j]:
            continue
        ans[j] = min(ans[j],arr[j])
    arr = []
    for j in range(n):
        q[j] ^= 1
        if q[j]:
            arr.append(j+1)
    print len(arr)
    sys.stdout.flush()
    print " ".join(map(str,arr))
    sys.stdout.flush()
    arr = list(map(int,raw_input().split()))
    for j in range(n):
        if q[j]:
            continue
        ans[j] = min(ans[j],arr[j])
    cnt *= 2
print -1
sys.stdout.flush()
print " ".join(map(str,ans))
sys.stdout.flush()
