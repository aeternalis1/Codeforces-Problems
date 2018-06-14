n,k = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
if k==1:
  print min(nums)
elif k==2:
  print max(nums[0],nums[-1])
else:
  print max(nums)
