n = int(raw_input())
a,b = map(int,raw_input().split())
spd = b
ans = 0
lim = []
take = 0
for i in range(n-1):
  q = raw_input()
  if q[0]=='1':
    a,b = map(int,q.split())
    spd = b
    while lim and lim[-1]<spd:
      ans += 1
      lim.pop(-1)
  elif q[0]=='3':
    a,b = map(int,q.split())
    if spd > b:
      ans += 1
    else:
      lim.append(b)
  else:
    a = int(q)
    if a==2:
      ans += take
      take = 0
    elif a==4:
      take = 0
    elif a==5:
      lim = []
    else:
      take += 1
print ans
