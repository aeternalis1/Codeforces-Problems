n,k = map(int,raw_input().split())
nums = sorted(list(map(int,raw_input().split())),reverse=True)
a = n
b = n*2
for i in range(k):
  if nums[i] >= 4 and a:
    cur = min(a,nums[i]/4)
    a -= cur
    nums[i] -= cur*4
for i in range(k):
  if nums[i] >= 3 and a:
    cur = min(a,nums[i]/3)
    a -= cur
    nums[i] -= cur*3
a1 = a
a2 = a
for i in range(k):
  if nums[i] >= 2 and b:
    cur = min(b,nums[i]/2)
    b -= cur
    nums[i] -= cur*2
  elif nums[i] >= 2 and a1:
    cur = min(a1,nums[i]/2)
    a1 -= cur
    nums[i] -= cur*2
for i in range(k):
  if nums[i] and a2:
    cur = min(a2,nums[i])
    a2 -= cur
    nums[i] -= cur
  elif nums[i] and b:
    nums[i] -= 1
    b -= 1
  elif nums[i] and a1:
    a1 -= 1
    nums[i] -= 1
if sum(nums):
  print "NO"
else:
  print "YES"
