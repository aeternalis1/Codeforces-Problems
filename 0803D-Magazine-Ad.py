k = int(raw_input())
s = raw_input().replace('-',' ')
s = s.split()
s = [len(x)+1 for x in s]
s[-1] -= 1
n = len(s)
lo = max(s)
hi = 1000001
while lo < hi:
  mid = (lo+hi)/2
  cur = 0
  cnt = 1
  for i in range(n):
    if s[i]+cur>mid:
      cur = s[i]
      cnt += 1
    else:
      cur += s[i]
  if cnt > k:
    lo = mid+1
  else:
    hi = mid
print lo
