n = int(raw_input())
nums = list(map(int,raw_input().split()))
swap = [int(x) for x in list(raw_input())]
taken = []
found = 0
for i in range(n):
  taken.append(nums[i])
  if i < n-1 and not swap[i]:
    if sorted(taken) != [x+1 for x in range(i-len(taken)+1,i+1)]:
      found = 1
    taken = []
if taken:
  if sorted(taken) != [x+1 for x in range(n-len(taken),n)]:
    found = 1
if found:
  print "NO"
else:
  print "YES"
