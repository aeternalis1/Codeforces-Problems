x,k = map(int,raw_input().split())
if x==0:
  print 0
else:
  ans = x*pow(2,k+1,1000000007)-pow(2,k,1000000007)+1
  print ans%1000000007
