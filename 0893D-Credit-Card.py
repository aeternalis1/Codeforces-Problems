n,D = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
arr = [0 for x in range(n+1)]
arr[n-1] = max(nums[n-1],0)
for i in range(n-2,-1,-1):
  arr[i] = max(arr[i+1]+nums[i],0)
cur = 0
ans = 0
val = 1
for i in range(n):
  if nums[i]==0:
    if cur < 0:
      cur = D-arr[i]
      ans += 1
    if cur < 0:
      val = 0
  cur += nums[i]
  if cur > D:
    val = 0
if not val:
  print -1
else:
  print ans
