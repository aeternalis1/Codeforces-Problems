n = int(raw_input())
s = list(raw_input())
t = list(raw_input())
par = [x for x in range(26)]
rank = [0 for x in range(26)]
size = [1 for x in range(26)]

al = "abcdefghijklmnopqrstuvwxyz"

def parent(i):
  if par[i]==i:
    return i
  return parent(par[i])

def merge(a,b):
  if rank[a] > rank[b]:
    par[b] = a
    size[a] += size[b]
  elif rank[b] > rank[a]:
    par[a] = b
    size[b] += size[a]
  else:
    rank[b] += 1
    par[a] = b
    size[b] += size[a]

ans = 0
fin = []

for i in range(n):
  a,b = al.index(s[i]),al.index(t[i])
  c,d = parent(a),parent(b)
  if c==d:
    continue
  merge(c,d)
  ans += 1
  fin.append([al[c],al[d]])

print ans
for i in fin:
  print " ".join(i)
