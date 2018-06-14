from __future__ import division
import sys
R,x1,y1,x2,y2 = map(int,raw_input().split()) #radius of flat, coords of flat, coords of fafa

if (abs(y2-y1)**2+abs(x2-x1)**2)**0.5 >= R: #if fafa outside of circle
  print x1,y1,R
else: #find distance to center, that plus radius == new diameter
  dist = (abs(y2-y1)**2+abs(x2-x1)**2)**0.5
  r = (dist+R)/2
  if x1 == x2:
    slope = None
    if y2 > y1:
      print x2,y2-r,r
    else:
      print x2,y2+r,r
    sys.exit()
  else:
    slope = (y2-y1)/(x2-x1)
  if slope == 0:
    if x2 > x1:
      print x2-r,y2,r
    else:
      print x2+r,y2,r
    sys.exit()
  x = x2+((x1-x2)*(1/(dist/(r*2))))/2
  y = y2+((y1-y2)*(1/(dist/(r*2))))/2
  print x,y,r
