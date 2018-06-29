n = int(raw_input())
nums = list(map(int,raw_input().split()))
ans = -1
valid = 1
pos = []
for i in range(n-1):
  if (nums[i]==nums[i+1]):
    valid = 0
    ans = 1
  if abs(nums[i]-nums[i+1]) != 1:
    if ans==-1:
      ans = abs(nums[i]-nums[i+1])
    else:
      if abs(nums[i]-nums[i+1]) != ans:
        valid = 0
  else:
    if ans==-1:
      pos.append([nums[i],nums[i+1]])
    else:
      if (nums[i]-1)/ans != (nums[i+1]-1)/ans:
        valid = 0
if ans != -1:
  for i in pos:
    if (i[0]-1)/ans != (i[1]-1)/ans:
      valid = 0
else:
  ans = pow(10,9)
if valid:
  print "YES"
  print pow(10,9),ans
else:
  print "NO"
