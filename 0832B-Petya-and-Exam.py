s = list(raw_input())
lets = 'abcdefghijklmnopqrstuvwxyz'
good = [0 for x in range(26)]
for i in s:
  good[lets.find(i)] = 1
pat = raw_input()
n = int(raw_input())
m = len(pat)
have = 0
if '*' in pat:
  have = 1
  a,b = pat.split('*')
  a1 = len(a)
  b1 = len(b)
for i in range(n):
  s = list(raw_input())
  val = 1
  cur = len(s)
  if not have:
    if len(s) != m:
      val = 0
    else:
      for j in range(m):
        if pat[j]=='?' and not good[lets.find(s[j])]:
          val = 0
        elif pat[j] != '?' and pat[j] != s[j]:
          val = 0
  else:
    if cur < m-1:
      val = 0
    try:
      for j in range(a1):
        if a[j]=='?' and not good[lets.find(s[j])]:
          val = 0
        elif a[j] != '?' and a[j] != s[j]:
          val = 0
      for j in range(b1):
        if b[b1-j-1]=='?' and not good[lets.find(s[cur-j-1])]:
          val = 0
        elif b[b1-j-1] != '?' and b[b1-j-1] != s[cur-j-1]:
          val = 0
      for j in range(a1,cur-b1):
        if good[lets.find(s[j])]:
          val = 0
    except:
      val = 0
  if not val:
    print "NO"
  else:
    print "YES"
