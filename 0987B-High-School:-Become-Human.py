from __future__ import division
from math import log
a,b = map(int,raw_input().split())
if log(a)/a > log(b)/b:
  print ">"
elif log(a)/a==log(b)/b:
  print '='
else:
  print "<"
