k,n = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
arr = list(map(int,raw_input().split()))
inds = {}
for i in range(n):
  inds[arr[i]] = i
ans = []
for i in range(1,k+1):
  checked = [0 for x in range(n)]
  checked[0] = 1
  cur = arr[0]
  for j in range(i,k):
    cur += nums[j]
    try:
      checked[inds[cur]] = 1
    except:
      None
  cur = arr[0]
  for j in range(i-1,-1,-1):
    cur -= nums[j]
    if j != 0:
      try:
        checked[inds[cur]] = 1
      except:
        None
  if 0 in checked:
    continue
  else:
    ans.append(cur)
print len(set(ans))
