n = int(raw_input())
s = list(raw_input())
dp = [[0,0,0] for x in range(n)]
found = False
ans = False
for i in range(1,n):
  if s[i]==s[i-1] and s[i] != '?':
    found = True
  if s[i]==s[i-1] and s[i] == '?':
    ans = True
for i in range(n):
  if s[i] == '?':
    if i == 0:
      ans = True
    elif i == n-1:
      ans = True
    else:
      if s[i-1]==s[i+1]:
        ans = True
if ans and not found:
  print "Yes"
else:
  print "No"
