n,m = map(int,raw_input().split())
nums = [0]+list(map(int,raw_input().split()))
par = [x for x in range(n+1)]
rank = [0 for x in range(n+1)]
ans = sum(nums)
def parent(a):
  if par[a]==a:
    return a
  return parent(par[a])

def merge(a,b):
  if rank[a]>rank[b]:
    par[b] = a
    nums[a] = min(nums[a],nums[b])
  elif rank[a]<rank[b]:
    par[a] = b
    nums[b] = min(nums[a],nums[b])
  else:
    rank[a] += 1
    par[b] = a
    nums[a] = min(nums[a],nums[b])

for i in range(m):
  a,b = map(int,raw_input().split())
  a,b = parent(a),parent(b)
  if a==b:
    continue
  ans -= max(nums[a],nums[b])
  merge(a,b)

print ans
