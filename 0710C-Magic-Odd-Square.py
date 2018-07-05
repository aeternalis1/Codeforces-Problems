n = int(raw_input())
arr = [[0 for x in range(n)] for x in range(n)]
cnt = 1
for i in range(n):
  cur = abs(n/2-i)
  for j in range(cur,n-cur):
    arr[i][j] = cnt
    cnt += 2
cnt = 2
for i in range(n):
  for j in range(n):
    if not arr[i][j]:
      arr[i][j] = cnt
      cnt += 2
for i in arr:
  print " ".join([str(x) for x in i])
