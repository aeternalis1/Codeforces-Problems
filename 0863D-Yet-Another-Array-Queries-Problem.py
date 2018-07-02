N,Q,M = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
qs = []
for i in range(Q):
  qs.append(list(map(int,raw_input().split())))
arr = list(map(int,raw_input().split()))
ans = [0 for x in range(M)]
for i in range(M):
  cur = arr[i]
  for j in range(Q-1,-1,-1):
    if qs[j][0]==1:
      if qs[j][1] <= cur and qs[j][2] >= cur:
        if cur==qs[j][1]:
          cur = qs[j][2]
        else:
          cur -= 1
    else:
      if qs[j][1] <= cur and qs[j][2] >= cur:
        cur = qs[j][2]-(cur-qs[j][1])
  ans[i] = nums[cur-1]
print " ".join([str(x) for x in ans])
