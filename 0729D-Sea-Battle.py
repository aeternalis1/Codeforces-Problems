n,a,b,k = map(int,raw_input().split())
nums = [int(x) for x in list(raw_input())]
cnt = 0
ans = 0
taken = []
for i in range(n):
  if nums[i]:
    cnt = 0
  else:
    cnt += 1
    if cnt == b:
      ans += 1
      taken.append(i+1)
      nums[i] = 1
      cnt = 0
print ans-a+1
print " ".join([str(x) for x in taken[:ans-a+1]])
