N,Q,C = map(int,raw_input().split())
arr = [[[0 for x in range(C+1)] for x in range(102)] for x in range(102)]
for i in range(N):
  a,b,c = map(int,raw_input().split())
  for j in range(C+1):
    arr[b][a][j] += (c+j)%(C+1)
for i in range(1,102):
  for j in range(1,102):
    for k in range(C+1):
      arr[i][j][k] += arr[i][j-1][k]
for i in range(1,102):
  for j in range(1,102):
    for k in range(C+1):
      arr[i][j][k] += arr[i-1][j][k]
for i in range(Q):
  a,b,c,d,e = map(int,raw_input().split())
  a %= (C+1)
  print arr[e][d][a]+arr[c-1][b-1][a]-arr[e][b-1][a]-arr[c-1][d][a]
