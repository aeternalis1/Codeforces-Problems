n = int(raw_input())
nums = list(map(int,raw_input().split()))
nums = sorted(nums)
nums = [x-1 for x in nums]
taken = [0 for x in range(n)]
ans = 0
ans2 = 0
ind = 0
for i in range(n):
  if i%2:
    ans2 += abs(nums[ind]-i)
    ind += 1
  else:
    ans += abs(nums[ind]-i)
print min(ans,ans2)
