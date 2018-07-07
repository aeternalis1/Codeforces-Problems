n,m = map(int,raw_input().split())
s = list(raw_input())
t = list(raw_input())
ans = 10000
fin = []
for i in range(m-n+1):
  res = []
  for j in range(n):
    if s[j] != t[i+j]:
      res.append(j+1)
  if len(res)<ans:
    ans = len(res)
    fin = [x for x in res]
print ans
print " ".join([str(x) for x in fin])
