n,m = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
nums2 = sorted(nums)
arr = []
for i in range(m):
  a,b = map(int,raw_input().split())
  arr.append([b,a,i])
arr = sorted(arr,reverse=True)+[[0,0,1000000]]
last = arr[0]
if arr[0][1]==1:
  nums[:arr[0][0]] = sorted(nums[:arr[0][0]])
else:
  nums[:arr[0][0]] = sorted(nums[:arr[0][0]],reverse=True)
tmp = sorted(nums[:arr[0][0]])
l = 0
r = arr[0][0]-1
for i in range(1,m+1):
  if arr[i][2] < last[2]:
    continue
  if last[1]==2:
    for j in range(last[0]-1,arr[i][0]-1,-1):
      nums[j] = tmp[l]
      l += 1
  else:
    for j in range(last[0]-1,arr[i][0]-1,-1):
      nums[j] = tmp[r]
      r -= 1
  last = arr[i]
print " ".join([str(x) for x in nums])
