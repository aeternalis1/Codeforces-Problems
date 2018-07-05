from __future__ import division
M,R = map(int,raw_input().split())
dist = pow(pow(R,2)+pow(R,2),0.5)
nums = [0 for x in range(M)]
for i in range(M):
  if i > 1:
    nums[i] = 2*R+dist*2+R*2*(i-2)
  elif i==1:
    nums[i] = R*2+dist
  else:
    nums[i] = R*2
ans = 0
cur = pow(M,2)
for i in range(M):
  if i:
    ans += (nums[i]*(M-i)*2)/cur
  else:
    ans += (nums[i]*M)/cur
print ans
