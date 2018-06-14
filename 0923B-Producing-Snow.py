N = int(raw_input())
nums = list(map(int,raw_input().split()))
temp = list(map(int,raw_input().split()))
nums2 = [0]+temp
arr = [0 for x in range(N+1)]
arr2 = [0 for x in range(N+1)]
for i in range(1,N+1):
  nums2[i] += nums2[i-1]
for i in range(N):
  lo = i+1
  hi = N+1
  while lo < hi:
    mid = (lo+hi)/2
    if nums2[mid]-nums2[i] >= nums[i]:
      hi = mid
    else:
      lo = mid+1
  lo -= 1
  arr[i] += 1
  arr[lo] -= 1
  arr2[lo] += nums[i]-(nums2[lo]-nums2[i])
cur = 0
ans = []
for i in range(N):
  cur += arr[i]
  ans.append(temp[i]*cur+arr2[i])
print " ".join([str(x) for x in ans])
