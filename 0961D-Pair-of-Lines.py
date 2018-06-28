from __future__ import division
import sys
n = int(raw_input())
if n <= 4:
  print "YES"
  sys.exit()
pts = []
for i in range(n):
  pts.append(list(map(int,raw_input().split())))

def solve(c1, c2):
  taken = [0 for x in range(n)]
  ext = []
  for i in range(n):
    if (pts[c2][1]-pts[c1][1])*(pts[i][0]-pts[c2][0])==(pts[i][1]-pts[c2][1])*(pts[c2][0]-pts[c1][0]):
      taken[i] = 1
    if not taken[i]:
      ext.append(i)
  if len(ext) <= 2:
    return 1
  c1 = ext[0]
  c2 = ext[1]
  for i in range(n):
    if (pts[c2][1]-pts[c1][1])*(pts[i][0]-pts[c2][0])==(pts[i][1]-pts[c2][1])*(pts[c2][0]-pts[c1][0]):
      taken[i] = 1
  if sum(taken)==n:
    return 1
  return 0

if solve(0,1) or solve(0,2) or solve(1,2):
  print "YES"
else:
  print "NO"
