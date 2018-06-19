import sys
n,k,m = map(int,raw_input().split())
mods = [[] for x in range(m)]
nums = list(map(int,raw_input().split()))
for i in range(n):
  mods[nums[i]%m].append(nums[i])
for i in range(m):
  if len(mods[i])>=k:
    print "Yes"
    print " ".join([str(x) for x in mods[i][:k]])
    sys.exit()
print "No"
