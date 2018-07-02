s = list(raw_input())
N = len(s)
i = 1
l = 0
vow = ['a','e','i','o','u']
ans = []
while i < N-1:
  if s[i] not in vow and s[i-1] not in vow and s[i+1] not in vow:
    if len(set(s[i-1:i+2]))>=2:
      ans.append("".join(s[l:i+1]))
      l = i+1
      i += 1
  i += 1
if l != N:
  ans.append("".join(s[l:N]))
print " ".join(ans)
