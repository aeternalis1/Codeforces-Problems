n = int(raw_input())
pos = [0,0]
ans = 0
s = raw_input()
moves = []
for i in range(n):
  q = s[i]
  if q == 'U':
    pos[1] += 1
  elif q == 'R':
    pos[0] += 1
  if pos[0] > pos[1]:
    moves.append(0)
  elif pos[0] == pos[1]:
    moves.append(1)
  else:
    moves.append(2)
for i in range(1,n-1):
  if moves[i] == 1:
    if moves[i-1] != moves[i+1]:
      ans += 1
print ans
