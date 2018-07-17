n = int(raw_input())
s = list(raw_input())
t = list(raw_input())
ans = 0
for i in range(n/2):
  li = [s[i],s[n-i-1]]
  li2 = [t[i],t[n-i-1]]
  if li==li2:
    continue
  big = li+li2
  big = sorted(big)
  if big.count(big[0])==2 and big.count(big[-1])==2:
    continue
  li = sorted(li)
  li2 = sorted(li2)
  if li[0]==li2[0] or li[0]==li2[1] or li[1]==li2[0] or li[1]==li2[1]:
    ans += 1
  elif li2[0]==li2[1]:
    ans += 1
  else:
    ans += 2
if n%2 and s[n/2]!=t[n/2]:
  ans += 1
print ans
