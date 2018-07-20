n = int(raw_input())
nums = sorted(list(map(int,raw_input().split())))
cur = 1
mod = pow(10,9)+7
ans = 0
for i in range(1,n):
  ans = (ans+cur*nums[i])%mod
  cur = (cur*2+1)%mod
cur = 1
for i in range(n-2,-1,-1):
  ans = (ans-cur*nums[i])%mod
  cur = (cur*2+1)%mod
print ans%mod
