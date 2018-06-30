n = int(raw_input())
nums = list(map(int,raw_input().split()))
temp = sorted(nums)
ans = [0 for x in range(n)]
for i in range(n):
  ans[nums.index(temp[i])] = temp[(i+1)%n]
print " ".join([str(x) for x in ans])
