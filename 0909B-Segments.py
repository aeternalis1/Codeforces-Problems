N = int(raw_input())
segs = []
for i in range(N):
  for j in range(i+1,N+1):
    segs.append([i,j])
ans = 0
while segs:
  curr = segs.pop(0)
  take = []
  for i in segs:
    if curr[1] <= i[0]:
      curr = i
      take.append(i)
  for i in take:
    segs.remove(i)
  ans += 1
print ans
