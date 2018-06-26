import sys
n = int(raw_input())
nums = list(map(int,raw_input().split()))
if (max(nums)-min(nums)) < 2:
  print n
  print " ".join([str(x) for x in nums])
  sys.exit()
tot = sum(nums)
arr = [min(nums),min(nums)+1,max(nums)]
arr2 = [nums.count(arr[0]),nums.count(arr[1]),nums.count(arr[2])]
ans = []
if tot > arr[1]*n:
  ans = ans+[arr[2]]*abs(tot-arr[1]*n)
  arr2[2] -= abs(tot-arr[1]*n)
  n -= abs(tot-arr[1]*n)
elif tot < arr[1]*n:
  ans = ans+[arr[0]]*abs(arr[1]*n-tot)
  arr2[0] -= abs(tot-arr[1]*n)
  n -= abs(tot-arr[1]*n)
if n%2:
  ans.append(arr[1])
  n -= 1
  arr2[1] -= 1
if arr2[1] < arr2[0]+arr2[2]:
  ans = ans+[arr[1]]*n
else:
  ans = ans+[arr[0]]*(n/2)
  ans = ans+[arr[2]]*(n/2)
print min(nums.count(arr[0]),ans.count(arr[0]))+min(nums.count(arr[1]),ans.count(arr[1]))+min(nums.count(arr[2]),ans.count(arr[2]))
print " ".join([str(x) for x in ans])
