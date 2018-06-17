from __future__ import division
nums = list(map(int,raw_input().split()))
nums2 = list(map(int,raw_input().split()))
s1 = [[nums[0],nums[1]],[nums[2],nums[3]],[nums[4],nums[5]],[nums[6],nums[7]]]
s2 = [[nums2[0],nums2[1]],[nums2[2],nums2[3]],[nums2[4],nums2[5]],[nums2[6],nums2[7]]]
lines = [[s1[0],s1[1]],[s1[1],s1[2]],[s1[2],s1[3]],[s1[3],s1[0]]]
lines2 = [[s2[0],s2[1]],[s2[1],s2[2]],[s2[2],s2[3]],[s2[3],s2[0]]]

ans = 0

minx = min(s1[0][0],s1[1][0],s1[2][0],s1[3][0])
maxx = max(s1[0][0],s1[1][0],s1[2][0],s1[3][0])
miny = min(s1[0][1],s1[1][1],s1[2][1],s1[3][1])
maxy = max(s1[0][1],s1[1][1],s1[2][1],s1[3][1])

for i in s2:
  if i[0] >= minx and i[0] <= maxx and i[1] >= miny and i[1] <= maxy:
    ans = 1

area = pow(s2[0][0]-s2[1][0],2)+pow(s2[0][1]-s2[1][1],2)

def triangle(num,num1,num2):
  try:
    a = pow((num[0]-num1[0])**2+(num[1]-num1[1])**2,0.5)
    b = pow((num[0]-num2[0])**2+(num[1]-num2[1])**2,0.5)
    c = pow((num1[0]-num2[0])**2+(num1[1]-num2[1])**2,0.5)
    s = (a+b+c)/2
  except:
    return 0
  try:
    return pow(s*(s-a)*(s-b)*(s-c),0.5)
  except:
    return 0;

for i in s1:
  res = 0
  for j in lines2:
    res += triangle(i,j[0],j[1])
  if abs(res-area)<=0.00001:
    ans = 1

midx = (minx+maxx)/2
midy = (miny+maxy)/2
res = 0
for j in lines2:
  res += triangle([midx,midy],j[0],j[1])
if abs(res-area)<=0.00001:
  ans = 1

if ans:
  print "YES"
else:
  print "NO"
