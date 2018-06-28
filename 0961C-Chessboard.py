n = int(raw_input())
grid = [[] for x in range(4)]
for i in range(4):
  for j in range(n):
    grid[i].append(list(raw_input()))
  if i < 3:
    raw_input()
ans = 999999
for i in range(4): #top left
  for j in range(4): #top right
    for k in range(4): #bottom left
      for l in range(4): #bottom right
        if len(set([i,j,k,l]))==4:
          ans1 = 0
          ans2 = 0
          for x in range(n):
            for y in range(n):
              if grid[i][x][y] == str((y+x)%2):
                ans1 += 1
              else:
                ans2 += 1
          for x in range(n):
            for y in range(n):
              if grid[l][x][y] == str((y+x)%2):
                ans1 += 1
              else:
                ans2 += 1
          for x in range(n):
            for y in range(n):
              if grid[j][x][y] != str((y+x)%2):
                ans1 += 1
              else:
                ans2 += 1
          for x in range(n):
            for y in range(n):
              if grid[k][x][y] != str((y+x)%2):
                ans1 += 1
              else:
                ans2 += 1
          ans = min(ans,ans1,ans2)
print ans
