n = int(raw_input())
primes = []
prime = [0 for x in range(10000)]
for i in range(2,10000):
  if not prime[i]:
    primes.append(i)
    for j in range(i+i,10000,i):
      prime[j] = 1
cnt = 0
ans = []
found = 1
while found:
  found = 0
  temp = n-cnt
  for i in range(2,int(pow(temp,0.5))+1):
    if (temp%i==0):
      found = 1
  cnt += 1
n -= temp
ans.append(temp)
if n:
  if not prime[n]:
    ans.append(n)
  else:
    for i in primes:
      if not prime[n-i]:
        ans.append(i)
        ans.append(n-i)
        break
print len(ans)
print " ".join([str(x) for x in ans])
