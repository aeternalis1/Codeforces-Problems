N,S = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
lo = 0
hi = N
while lo <= hi:
  mid = (lo+hi)/2
  temp = []
  for i in range(N):
    temp.append((i+1)*mid+nums[i])
  temp = sorted(temp)
  cur = 0
  for i in range(mid):
    cur += temp[i]
  if cur <= S:
    lo = mid+1
  else:
    hi = mid-1
lo -= 1
temp = []
for i in range(N):
  temp.append((i+1)*lo+nums[i])
temp = sorted(temp)
cur = 0
for i in range(lo):
  cur += temp[i]
print lo,cur
