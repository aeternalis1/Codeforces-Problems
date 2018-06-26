n = int(raw_input())
nums = list(map(int,raw_input().split()))
cur = 1
ans = 0
arr = [0 for x in range(n)]
for i in range(1,n):
  arr[i] = max(nums[i],arr[i-1])
for i in range(n-1,-1,-1):
  cur = max(cur-1,arr[i])
  ans += cur-nums[i]
print ans
