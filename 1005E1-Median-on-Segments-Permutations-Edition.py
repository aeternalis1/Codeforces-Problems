n,m = list(map(int,raw_input().split()))
nums = list(map(int,raw_input().split()))
ind = nums.index(m)
arr = [0 for x in range(n)]
cnt = {}
cnt2 = {}
for i in range(ind,n):
  if nums[i] > m:
    arr[i] += 1
  elif nums[i] < m:
    arr[i] -= 1
  arr[i] += arr[i-1]
  if i%2:
    try:
      cnt[arr[i]] += 1
    except:
      cnt[arr[i]] = 1
  else:
    try:
      cnt2[arr[i]] += 1
    except:
      cnt2[arr[i]] = 1
for i in range(ind,-1,-1):
  if i < ind:
    arr[i] += arr[i+1]
  if nums[i] > m:
    arr[i] += 1
  elif nums[i] < m:
    arr[i] -= 1
ans = 0
for i in range(ind+1):
  try:
    ans += cnt[-arr[i]]
  except:
    None
  try:
    ans += cnt2[-arr[i]]
  except:
    None
  if arr[i] < 0:
    if i%2:
      try:
        ans += cnt2[-arr[i]+1]
      except:
        None
    else:
      try:
        ans += cnt[-arr[i]+1]
      except:
        None
  else:
    if i%2:
      try:
        ans += cnt2[-arr[i]+1]
      except:
        None
    else:
      try:
        ans += cnt[-arr[i]+1]
      except:
        None
print ans
