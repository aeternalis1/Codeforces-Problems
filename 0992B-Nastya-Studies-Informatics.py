l,r,x,y = map(int,raw_input().split())
facts = []

def gcd(a,b):
  if not b:
    return a
  if a%b==0:
    return b
  return gcd(b,a%b)

for i in range(1,int(pow(y,0.5))+1):
  if y%i==0:
    facts.append(i)
    facts.append(y/i)
facts = list(set(facts))
ans = 0
for i in range(len(facts)):
  for j in range(len(facts)):
    if facts[i] >= l and facts[i] <= r and facts[j] >= l and facts[j] <= r:
      if gcd(facts[i],facts[j])==x:
        if facts[i]*facts[j]/x==y:
          ans += 1
print ans
