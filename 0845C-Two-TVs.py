n = int(raw_input())
arr = []
for i in range(n):
  arr.append(list(map(int,raw_input().split())))
arr = sorted(arr)
rs = [-1,-1]
val = 1
for i in range(n):
  if rs[0] < arr[i][0]:
    rs[0] = arr[i][1]
  elif rs[1] < arr[i][0]:
    rs[1] = arr[i][1]
  else:
    val = 0
if val:
  print "YES"
else:
  print "NO"
