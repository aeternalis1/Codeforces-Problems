n = int(raw_input())
nums = list(map(int,raw_input().split()))
need = [0 for x in range(n+1)]
seen = [0 for x in range(n+1)]
for i in nums:
  need[i] += 1
arr = []
for i in range(1,n+1):
  if not need[i]:
    arr.append(i)
ind = 0
N = len(arr)
for i in range(n):
  if need[nums[i]]>1:
    if arr[ind]<nums[i]:
      need[nums[i]] -= 1
      nums[i] = arr[ind]
      ind += 1
    elif seen[nums[i]]:
      need[nums[i]] -= 1
      nums[i] = arr[ind]
      ind += 1
    else:
      seen[nums[i]] = 1
print N
print " ".join([str(x) for x in nums]) 
