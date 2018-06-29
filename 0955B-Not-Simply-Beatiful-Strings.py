s = raw_input()
cnt = [0 for x in range(26)]
lets = 'abcdefghijklmnopqrstuvwxyz'
dist = []
for i in range(len(s)):
  if cnt[lets.find(s[i])]==0:
    dist.append(s[i])
  cnt[lets.find(s[i])] += 1
if len(dist)>4 or len(dist)==1:
  print "No"
elif len(dist)==2 and len(s)-max(cnt)==1:
  print "No"
elif len(dist)==3 and max(cnt)==1:
  print "No"
else:
  print "Yes"
