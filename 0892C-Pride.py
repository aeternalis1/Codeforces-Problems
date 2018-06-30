n = int(raw_input())
nums = list(map(int,raw_input().split()))

def gcd(a,b):
  if a==0:
    return b
  if b==0:
    return a
  if a%b==0:
    return b
  return gcd(b,a%b)

ans = 99999
if 1 in nums:
  ans = 1
for i in range(n):
  cur = nums[i]
  for j in range(i+1,n):
    cur = gcd(cur,nums[j])
    if cur==1:
      ans = min(ans,j-i)
      break

if ans==99999:
  print -1
else:
  print n+ans-1-nums.count(1)
