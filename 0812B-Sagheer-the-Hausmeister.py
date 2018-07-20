n,m = map(int,raw_input().split())
grid = []
arr = [[m+1,0] for x in range(n)]
for i in range(n):
  grid.append(list(raw_input()))
last = -1
f = 0
for i in range(n):
  for j in range(1,m+1):
    if grid[i][j]=='1':
      arr[i][0] = min(arr[i][0],j)
      arr[i][1] = j
  if '1' in grid[i]:
    f = 1
  if not f:
    last += 1
left = 0
right = 99999
for i in range(n-1,-1,-1):
  if i==last:
    break
  if i==last+1:
    left = left+arr[i][1]
    right = right+(m+1-arr[i][0])
  else:
    left,right = min(arr[i][1]*2+left,right+m+1)+1,min((m+1-arr[i][0])*2+right,left+m+1)+1
print min(left,right)
