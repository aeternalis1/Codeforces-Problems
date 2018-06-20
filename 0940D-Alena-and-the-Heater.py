N = int(raw_input())
nums = list(map(int,raw_input().split()))
nums2 = [int(x) for x in list(raw_input())]
l = -pow(10,9)
r = pow(10,9)
for i in range(4,N):
  if len(set(nums2[i-4:i]))==1 and nums2[i-1] != nums2[i]:
    if nums2[i]==0:
      r = min(min(nums[i-4:i+1])-1,r)
    else:
      l = max(max(nums[i-4:i+1])+1,l)
print l,r
    
