n,k = map(int,raw_input().split())
s = list(raw_input())
t = list(raw_input())
same = [0 for x in range(n)]
lets = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
  if s[i]==t[i]:
    same[i] = 1
ans = ['' for x in range(n)]
cnt = 0
cnt2 = 0
if sum(same) >= n-k:
  cur = sum(same)-n+k
  for i in range(n):
    if same[i] and cur:
      cur -= 1
    elif same[i]:
      ans[i] = s[i]
      continue
    for j in range(26):
      if lets[j] != s[i] and lets[j] != t[i]:
        ans[i] = lets[j]
        break
else:
  for i in range(n):
    if same[i]:
      ans[i] = s[i]
      continue
    if cnt > cnt2:
      ans[i] = s[i]
      cnt2 += 1
    else:
      ans[i] = t[i]
      cnt += 1
  for i in range(n):
    if cnt < k and cnt2 < k and same[i]:
      for j in range(26):
        if lets[j] != s[i] and lets[j] != t[i]:
          ans[i] = lets[j]
          break
      cnt += 1
      cnt2 += 1
    elif cnt < k and ans[i]==s[i] and not same[i]:
      for j in range(26):
        if lets[j] != s[i] and lets[j] != t[i]:
          ans[i] = lets[j]
          break
      cnt += 1
    elif cnt2 < k and ans[i]==t[i] and not same[i]:
      for j in range(26):
        if lets[j] != s[i] and lets[j] != t[i]:
          ans[i] = lets[j]
          break
      cnt2 += 1
if cnt > k or cnt2 > k:
  print -1
else:
  print "".join(ans)
