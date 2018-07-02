N,A,B = map(int,raw_input().split())
A -= 1
B -= 1
beat = [2,0,1]
grid1 = []
grid2 = []
for i in range(3):
  grid1.append(list(map(int,raw_input().split())))
  grid1[i] = [x-1 for x in grid1[i]]
for i in range(3):
  grid2.append(list(map(int,raw_input().split())))
  grid2[i] = [x-1 for x in grid2[i]]
checked = [[0 for x in range(3)] for x in range(3)]
sums = [[[0,0] for x in range(3)] for x in range(3)]
dist = [[0 for x in range(3)] for x in range(3)]
checked[A][B] = 1
ans = [0,0]
if beat[A]==B:
  sums[A][B] = [1,0]
  ans = [1,0]
elif beat[B]==A:
  sums[A][B] = [0,1]
  ans = [0,1]
dist[A][B] = 0
i = 1
while i < N:
  lastA,lastB,A,B = A,B,grid1[A][B],grid2[A][B]
  if checked[A][B]:
    cur = dist[lastA][lastB]-dist[A][B]+1
    temp = N-1-i
    if lastA != A or lastB != B:
      if beat[A]==B:
        sums[lastA][lastB][0] += 1
      elif beat[B]==A:
        sums[lastA][lastB][1] += 1
      ans[0] += (sums[lastA][lastB][0]-sums[A][B][0])*(temp/cur)
      ans[1] += (sums[lastA][lastB][1]-sums[A][B][1])*(temp/cur)
    else:
      if beat[A]==B:
        ans[0] += temp
      elif beat[B]==A:
        ans[1] += temp
    i = N-1-temp%cur
    checked = [[0 for x in range(3)] for x in range(3)]
  checked[A][B] = 1
  if beat[A]==B:
    sums[A][B] = [sums[lastA][lastB][0]+1,sums[lastA][lastB][1]]
    ans[0] += 1
  elif beat[B]==A:
    sums[A][B] = [sums[lastA][lastB][0],sums[lastA][lastB][1]+1]
    ans[1] += 1
  else:
    sums[A][B] = [x for x in sums[lastA][lastB]]
  dist[A][B] = i
  i += 1
print ans[0],ans[1]
