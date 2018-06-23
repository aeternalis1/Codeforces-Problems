from __future__ import division
s = list(raw_input())
ans = 0
lets = "abcdefghijklmnopqrstuvwxyz."
digs = "0123456789"
N = len(s)
i = 1
while i < N:
  if s[i-1] in lets and s[i] in digs:
    cur = 0
    while i < N:
      while i < N and s[i] not in lets:
        cur *= 10
        cur += int(s[i])
        i += 1
      if i >= N:
        break
      if s[i]=='.':
        i += 1
      else:
        break
      mult = 1
      while i < N and s[i] in digs:
        cur *= 10
        cur += int(s[i])
        mult *= 10
        i += 1
      if mult == 100:
        cur /= mult
        break
    ans += cur
  else:
    i += 1
ans = list(str(ans))
if ans[-2]=='.':
  ans.append('0')
final = []
cnt = 0
for i in range(len(ans)-1,-1,-1):
  if cnt==3:
    final.append('.')
    cnt = 1
    final.append(ans[i])
  else:
    if ans[i]=='.':
      cnt = 0
    else:
      cnt += 1
    final.append(ans[i])
if len(final)>3 and final[:3]==['0','0','.']:
  print "".join(final[3:][::-1])
else:
  print "".join(final[::-1])
