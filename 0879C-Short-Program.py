n = int(raw_input())
bits = [[0 for x in range(10)] for x in range(2)]
bits[1] = [1 for x in range(10)]
for i in range(n):
  a,b = raw_input().split()
  b = int(b)
  temp = [0 for x in range(10)]
  cur = 0
  while b:
    temp[cur] = b%2
    b /= 2
    cur += 1
  if a=='|':
    for j in range(10):
      if temp[j]:
        bits[0][j] = 1
        bits[1][j] = 1
  elif a=='^':
    for j in range(10):
      bits[0][j] ^= temp[j]
      bits[1][j] ^= temp[j]
  else:
    for j in range(10):
      bits[0][j] &= temp[j]
      bits[1][j] &= temp[j]
ans = [0,1023,0]
val = [0,0,0]
pr = '|&^'
for i in range(10):
  if bits[0][i] and bits[1][i]:
    ans[0] |= (1<<i)
    val[0] = 1
  elif not bits[1][i] and not bits[0][i]:
    ans[1] ^= (1<<i)
    val[1] = 1
  elif bits[0][i] and not bits[1][i]:
    ans[2] |= (1<<i)
    val[2] = 1
print sum(val)
for i in range(3):
  if val[i]:
    print pr[i],ans[i]
