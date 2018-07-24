s = sorted(list(raw_input()))
t = sorted(list(raw_input()),reverse=True)
n = len(s)
if n%2:
  s = s[:n/2+1]
  r1 = n/2
else:
  s = s[:n/2]
  r1 = n/2-1
t = t[:n/2]
ans = ['' for x in range(n)]
l,l1,l2 = 0,0,0
r,r2 = n-1,n/2-1
for i in range(n):
  if i%2==0:
    if i==n-1 or s[l1]<t[l2] or (s[l1]==t[l2] and s[l1]<t[r2]):
      ans[l] = s[l1]
      l1 += 1
      l += 1
    else:
      ans[r] = s[r1]
      r1 -= 1
      r -= 1
  else:
    if i==n-1 or t[l2]>s[l1]:
      ans[l] = t[l2]
      l2 += 1
      l += 1
    else:
      ans[r] = t[r2]
      r2 -= 1
      r -= 1
print "".join(ans)
