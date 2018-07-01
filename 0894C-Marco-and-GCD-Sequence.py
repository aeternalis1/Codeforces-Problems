n = int(raw_input())
nums = list(map(int,raw_input().split()))
def gcd(a,b):
  if a==0 or a%b==0:
    return b
  return gcd(b,a%b)
cur = nums[0]
for i in range(n):
  cur = gcd(nums[i],cur)
if cur != min(nums):
  print -1
else:
  print n*2-1
  ans = []
  for i in range(n):
    ans.append(str(min(nums)))
    ans.append(str(nums[i]))
  print " ".join(ans[1:])
