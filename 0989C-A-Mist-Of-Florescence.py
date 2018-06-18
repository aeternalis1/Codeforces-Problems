a,b,c,d = map(int,raw_input().split())
li = [a,b,c,d]
li[0] -= 1
li[1] -= 1
li[2] -= 1
li[3] -= 1
arr = [[0 for x in range(50)] for x in range(40)]
n = 40
m = 50
for i in range(10):
  for j in range(m):
    arr[i][j] = 'A'
for i in range(10,20):
  for j in range(m):
    arr[i][j] = 'B'
for i in range(20,30):
  for j in range(m):
    arr[i][j] = 'C'
for i in range(30,40):
  for j in range(m):
    arr[i][j] = 'D'
for i in range(1,9):
  for j in range(m):
    if i%2==j%2 and i%2:
      if li[1]:
        li[1] -= 1
        arr[i][j] = 'B'
for i in range(11,19):
  for j in range(m):
    if i%2==j%2 and i%2:
      if li[0]:
        li[0] -= 1
        arr[i][j] = 'A'
for i in range(21,29):
  for j in range(m):
    if i%2==j%2 and i%2:
      if li[3]:
        li[3] -= 1
        arr[i][j] = 'D'
for i in range(31,39):
  for j in range(m):
    if i%2==j%2 and i%2:
      if li[2]:
        li[2] -= 1
        arr[i][j] = 'C'
print n,m
for i in arr:
  print "".join(i)
