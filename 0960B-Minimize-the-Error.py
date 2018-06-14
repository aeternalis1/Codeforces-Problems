n,a,b = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
nums2 = list(map(int,raw_input().split()))
for i in range(a+b):
  temp = 0
  ind = 0
  for j in range(n):
    if abs(nums[j]-nums2[j]) > temp:
      temp = abs(nums[j]-nums2[j])
      ind = j
  if nums[ind] > nums2[ind]:
    nums[ind] -= 1
  elif nums2[ind] > nums[ind]:
    nums2[ind] -= 1
  else:
    nums2[ind] += 1
ans = 0
for i in range(n):
  ans += pow(nums[i]-nums2[i],2)
print ans
