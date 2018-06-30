s = list(raw_input())
pos = [[-1] for x in range(26)]
lets = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(s)):
  pos[lets.find(s[i])].append(i)
ans = 999999
for i in range(26):
  pos[i].append(len(s))
  res = -1
  for j in range(len(pos[i])-1):
    res = max(res,pos[i][j+1]-pos[i][j])
  ans = min(res,ans)
print ans
