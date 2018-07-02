N = int(raw_input())
cnt = {}
arr = []
for i in range(N):
  temp = raw_input()
  arr.append(temp)
  got = []
  for j in range(9):
    for k in range(j,9):
      if temp[j:k+1] in got:
        continue
      got.append(temp[j:k+1])
      try:
        cnt[temp[j:k+1]] += 1
      except:
        cnt[temp[j:k+1]] = 1
for i in range(N):
  res = 9
  ans = ''
  for j in range(9):
    for k in range(j,9):
      if cnt[arr[i][j:k+1]]==1:
        if k-j+1 <= res:
          res = k-j+1
          ans = arr[i][j:k+1]
  print ans
