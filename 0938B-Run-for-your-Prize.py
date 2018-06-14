n = int(raw_input())
nums = list(map(int,raw_input().split()))
ans = 0
for i in nums:
  ans = max(ans,min(abs(i-1),abs(i-1000000)))
print ans
