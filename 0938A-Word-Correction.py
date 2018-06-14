n = int(raw_input())
s = list(raw_input())
vow = "aeiouy"
ind = 0
while ind < len(s)-1:
  if s[ind] in vow and s[ind+1] in vow:
    s.pop(ind+1)
  else:
    ind += 1
print "".join(s)
