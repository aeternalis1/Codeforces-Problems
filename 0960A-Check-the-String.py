s = raw_input()
valid = True
if len(s) < 3:
  valid = False
for i in range(1,len(s)):
  if s[i-1]=='b' and s[i] == 'a' or s[i-1]=='c' and s[i] == 'a' or s[i-1]=='c' and s[i] == 'b':
    valid = False
if s.count('a')!=s.count('c') and s.count('b')!=s.count('c'):
  valid = False
if not s.count('a') or not s.count('b') or not s.count('c'):
  valid = False
if valid:
  print "YES"
else:
  print "NO"
