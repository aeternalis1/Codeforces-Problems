n = int(raw_input())
arr = list(raw_input())
dp = [[[0 for x in range(n+1)] for x in range(n+1)] for x in range(n+1)]
a,b,c = arr.count('B'),arr.count('G'),arr.count('R')
ans = [0,0,0]
final = 'BGR'

def solve(a,b,c):
  if sum([a,b,c])==1:
    ans[[a,b,c].index(1)] = 1
    return
  if dp[a][b][c]:
    return
  dp[a][b][c] = 1
  temp = [a,b,c]
  if a:
    if a>1:
      solve(a-1,b,c)
    if b:
      solve(a-1,b-1,c+1)
    if c:
      solve(a-1,b+1,c-1)
  if b:
    if b>1:
      solve(a,b-1,c)
    if c:
      solve(a+1,b-1,c-1)
  if c>1:
    solve(a,b,c-1)

solve(a,b,c)

print "".join([final[i] for i in range(3) if ans[i]])
