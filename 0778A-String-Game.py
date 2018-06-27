s = list(raw_input())
t = list(raw_input())
nums = list(map(int,raw_input().split()))
nums = [x-1 for x in nums]
N = len(nums)
M = len(t)
lo = 0
hi = N
while lo < hi:
  mid = (lo+hi)/2
  take = [0 for x in range(N)]
  for i in range(mid):
    take[nums[i]] = 1
  ind = 0
  found = 0
  for i in range(N):
    if not take[i] and s[i]==t[ind]:
      ind += 1
    if ind==M:
      found = 1
      break
  if found:
    lo = mid+1
  else:
    hi = mid
print lo-1
