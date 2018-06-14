import sys
a,b,f,k = map(int,raw_input().split())
gas = b
cnt = 0
side = 0
ans = 0
imp = 0
if f > b or a-f>b:
  imp = 1
if k>1 and (a-f)*2 > b:
  imp = 1
if k>2 and f*2 > b:
  imp = 1
if imp:
  print -1
  sys.exit()
while cnt < k:
  if side%2==0:
    if cnt==k-1:
      if a > gas:
        ans += 1
      break
    if a+(a-f)>gas:
      ans += 1
      gas = b-(a-f)
    else:
      gas -= a
  else:
    if cnt==k-1:
      if a > gas:
        ans += 1
      break
    if a+f>gas:
      ans += 1
      gas = b-f
    else:
      gas -= a
  side ^= 1
  cnt += 1
print ans
