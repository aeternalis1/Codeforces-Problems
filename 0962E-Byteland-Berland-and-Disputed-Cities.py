n = int(raw_input())
arr = [0 for x in range(n)]
disp = []
for i in range(n):
  a,b = raw_input().split()
  a = int(a)
  if b=='P':
    b = 0
    disp.append(i)
  elif b=='R':
    b = 1
  else:
    b = 2
  arr[i] = [a,b]
ans = 0
last = [None,None]
for i in range(n):
  if arr[i][1]==1 or arr[i][1]==0:
    if last[0] != None:
      ans += arr[i][0]-last[0]
    last = arr[i]
last = [None,None]
for i in range(n):
  if arr[i][1]==2 or arr[i][1]==0:
    if last[0] != None:
      ans += arr[i][0]-last[0]
    last = arr[i]
for i in range(len(disp)-1):
  if disp[i+1]-disp[i] == 1:
    ans -= arr[disp[i+1]][0]-arr[disp[i]][0]
    continue
  l1 = None
  l2 = None
  ans1 = 0
  ans2 = 0
  gap1 = 0
  gap2 = 0
  dist = [99999999999,99999999999]
  dist2 = [99999999999,99999999999]
  for j in range(disp[i]+1,disp[i+1]):
    if arr[j][1]==1:
      if l1 != None:
        ans1 += arr[j][0]-l1
        gap1 = max(gap1,arr[j][0]-l1)
      l1 = arr[j][0]
      dist[0] = min(dist[0],arr[j][0]-arr[disp[i]][0])
      dist[1] = min(dist[1],arr[disp[i+1]][0]-arr[j][0])
    else:
      if l2 != None:
        ans2 += arr[j][0]-l2
        gap2 = max(gap2,arr[j][0]-l2)
      l2 = arr[j][0]
      dist2[0] = min(dist2[0],arr[j][0]-arr[disp[i]][0])
      dist2[1] = min(dist2[1],arr[disp[i+1]][0]-arr[j][0])
  if l1 != None and l2 != None:
    cur1 = ans1-gap1+sum(dist)
    cur2 = ans2-gap2+sum(dist2)
    cur3 = ans1+min(dist)
    cur4 = ans2+min(dist2)
    ans = min(ans,ans-(arr[disp[i+1]][0]-arr[disp[i]][0])+min(cur1,cur3)+min(cur2,cur4))
  elif l1 != None:
    cur1 = ans1-gap1+sum(dist)
    ans = min(ans,ans-(arr[disp[i+1]][0]-arr[disp[i]][0])+min(ans1+min(dist),cur1))
  elif l2 != None:
    cur2 = ans2-gap2+sum(dist2)
    ans = min(ans,ans-(arr[disp[i+1]][0]-arr[disp[i]][0])+min(ans2+min(dist2),cur2))
print ans
