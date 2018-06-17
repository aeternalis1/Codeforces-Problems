n,m = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
nums2 = list(map(int,raw_input().split()))
ans = [0 for x in range(n)]
ans2 = [0 for x in range(m)]
digs = [0 for x in range(10)]
def check(a,b,c,d):
  if len(set([a,b,c,d]))==3:
    return 1
  if len(set([a,b,c,d]))==2:
    return -1
  return 0
temp = 0
for i in range(n):
  for j in range(m):
    res = check(nums[i*2],nums[i*2+1],nums2[j*2],nums2[j*2+1])
    if res==-1:
      continue
    ans[i] += res
    ans2[j] += res
    if res:
      if nums[i*2]==nums2[j*2] or nums[i*2]==nums2[j*2+1]:
        digs[nums[i*2]] += 1
      else:
        digs[nums[i*2+1]] += 1
if max(digs)==sum(digs) or sum(ans)==1 or sum(ans2)==1:
  print digs.index(max(digs))
else:
  res = 0
  for i in range(n):
    digs = [0 for x in range(10)]
    if ans[i] > 1:
      for j in range(m):
        if check(nums[i*2],nums[i*2+1],nums2[j*2],nums2[j*2+1]):
          if nums[i*2]==nums2[j*2] or nums[i*2]==nums2[j*2+1]:
            digs[nums[i*2]] += 1
          else:
            digs[nums[i*2+1]] += 1
    if max(digs) != sum(digs):
      res = 1
  for j in range(m):
    digs = [0 for x in range(10)]
    if ans2[j] > 1:
      for i in range(n):
        if check(nums[i*2],nums[i*2+1],nums2[j*2],nums2[j*2+1]):
          if nums[i*2]==nums2[j*2] or nums[i*2]==nums2[j*2+1]:
            digs[nums[i*2]] += 1
          else:
            digs[nums[i*2+1]] += 1
    if max(digs) != sum(digs):
      res = 1
  if res:
    print -1
  else:
    print 0
