n = int(raw_input())
s = list(raw_input())
ans = 0
for i in range(n):
  for j in range(i+1,n+1):
    cnt = [0 for x in range(26)]
    res = 1
    for k in range(i,j):
      if s[k].isupper():
        res = 0
        break
      else:
        cnt[ord(s[k])-ord('a')] = 1
    if res:
      ans = max(ans,sum(cnt))
print ans
