n,m = map(int,raw_input().split())
nums = [0]+list(map(int,raw_input().split()))+[m]

on = []
off = []
sum1 = [0 for x in range(n+2)]
sum2 = [0 for x in range(n+2)]
turns = [0 for x in range(n+2)]
for i in range(0,n+2,2):
  turns[i] = 1
for i in range(1,n+2):
  if i%2:
    on.append(nums[i]-nums[i-1])
    sum1[i] = sum1[i-1]+on[-1]
    sum2[i] = sum2[i-1]
  else:
    off.append(nums[i]-nums[i-1])
    sum1[i] = sum1[i-1]
    sum2[i] = sum2[i-1]+off[-1]
ans = sum1[-1]
for i in range(n+2):
  if i != 0 and nums[i]-1 != nums[i-1] and nums[i]-1 > 0:
    cur = nums[i]-1
    if turns[i]:
      res = sum2[-1]-sum2[i]+1+sum1[i]
    else:
      res = sum2[-1]-sum2[i]+sum1[i]-1
    ans = max(ans,res)
  if i != n+1 and nums[i]+1 != nums[i+1] and nums[i]+1 < m:
    cur = nums[i]+1
    if turns[i]:
      res = sum2[-1]-sum2[i]+sum1[i]+1
    else:
      res = sum2[-1]-sum2[i]+sum1[i]-1
    ans = max(ans,res)
print ans
