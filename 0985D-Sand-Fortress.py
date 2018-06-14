import sys
n,H = map(int,raw_input().split())

if n < H*(H+1)/2: #if first spot cant take H elements then descend
  lo = 1
  hi = H #binary search for the beginning element
  while lo < hi:
    mid = (lo+hi)/2
    if mid*(mid+1)/2 >= n:
      hi = mid
    else:
      lo = mid+1
  print lo
  sys.exit()

lo = 1
hi = 10000000000
ans = 9999999999999
while lo < hi:
  mid = (lo+hi)/2
  taken = mid*(mid+1)/2-H*(H-1)/2
  res = mid-H
  if taken > n:
    hi = mid
    continue
  temp = n-taken+mid
  temp2 = mid*(mid+1)/2
  if temp2 > temp:
    hi = mid
    continue
  temp -= temp2
  res += mid
  if temp%mid:
    res += temp/mid+1
  else:
    res += temp/mid
  ans = min(ans,res)
  lo = mid+1
print ans

#binary search on the peak, optimal solution will always include
#an nondecreasing portion that transfers to a nonincreasing portion that descends to 0

#greedily ascend directly to the peak, then descend however you want
