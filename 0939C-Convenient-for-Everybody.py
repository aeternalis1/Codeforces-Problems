n = int(raw_input())
nums = list(map(int,raw_input().split()))
nums = [0]+nums+nums
s,f = map(int,raw_input().split())
m = f-s
for i in range(2,n*2+1):
  nums[i] += nums[i-1]
ans = 0
res = 0
for i in range(m,n*2+1):
  if nums[i]-nums[i-m] > ans:
    ans = nums[i]-nums[i-m]
    res = [s-i+m]
  elif nums[i]-nums[i-m] == ans:
    res.append(s-i+m)
for i in range(len(res)):
  while res[i] <= 0:
    res[i] += n
print min(res)
