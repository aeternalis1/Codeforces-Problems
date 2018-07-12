arr = [int(x) for x in list(raw_input())]
fact = [1 for x in range(20)]
for i in range(2,20):
  fact[i] = i*fact[i-1]
cnt = [0 for x in range(10)]
for i in arr:
  cnt[i] += 1
ans = [0]
def solve(li,dep):
  if dep==-1:
    for i in range(10):
      if not li[i] and cnt[i]:
        return
    res = fact[sum(li)]
    for i in range(10):
      if li[i]:
        res /= fact[li[i]]
    if li[0]:
      res -= res*li[0]/sum(li)
    ans[0] += res
  else:
    for i in range(cnt[dep]+1):
      li[dep] = i
      solve(li,dep-1)
tmp = [0 for x in range(10)]
for i in range(cnt[9]+1):
  tmp[9] = i
  solve(tmp,8)
print ans[0]
