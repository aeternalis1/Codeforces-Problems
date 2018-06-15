n,m = map(int,raw_input().split())
arr = []
for i in range(n):
  temp = [9999,9999,9999]
  cur = list(raw_input())
  for j in range(m):
    if cur[j] >= '0' and cur[j] <= '9':
      temp[0] = min(j,temp[0],m-j)
    elif cur[j] >= 'a' and cur[j] <= 'z':
      temp[1] = min(j,temp[1],m-j)
    else:
      temp[2] = min(j,temp[2],m-j)
  arr.append(temp)
ans = 9999
for i in range(n):
  for j in range(n):
    for k in range(n):
      if i==j or j==k or i==k:
        continue
      ans = min(arr[i][0]+arr[j][1]+arr[k][2],ans)
print ans
