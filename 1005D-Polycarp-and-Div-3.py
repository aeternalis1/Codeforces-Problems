arr = [int(x)%3 for x in list(raw_input())]
n = len(arr)
nums = [0 for x in range(n)]
for i in range(n):
  nums[i] += arr[i]
  if i:
    nums[i] += nums[i-1]
ans = 0
have = [0,0,0]
for i in range(n):
  if arr[i]==0:
    have = [0,0,0]
    ans += 1
  else:
    if arr[i]==1 and have[2] or arr[i]==2 and have[1]:
      ans += 1
      have = [0,0,0]
      continue
    if arr[i]==1:
      if have[1]:
        have[2] = 1
      have[1] = 1
    else:
      if have[2]:
        have[1] = 1
      have[2] = 1
print ans
