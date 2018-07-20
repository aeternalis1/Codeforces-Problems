n = int(raw_input())
arr = list(map(int,raw_input().split()))
occ = {}
ans = 0
for i in range(n):
  cur = 0
  try:
    cur += occ[arr[i]+1]
  except:
    None
  try:
    cur += occ[arr[i]-1]
  except:
    None
  ans += arr[i]*(i-cur)
  try:
    occ[arr[i]] += 1
  except:
    occ[arr[i]] = 1
occ = {}
for i in range(n-1,-1,-1):
  cur = 0
  try:
    cur += occ[arr[i]+1]
  except:
    None
  try:
    cur += occ[arr[i]-1]
  except:
    None
  ans -= arr[i]*(n-i-cur-1)
  try:
    occ[arr[i]] += 1
  except:
    occ[arr[i]] = 1
print ans
