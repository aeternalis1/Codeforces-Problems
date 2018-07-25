n,x = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
cur = 1
cur2 = sum(nums) #number of factors of x
cnt = {}
for i in range(n):
  try:
    cnt[cur2-nums[i]] += 1
    temp = cur2-nums[i]
    try:
      while cnt[temp]==x:
        cnt[temp] = 0
        try:
          cnt[temp+1] += 1
        except:
          cnt[temp+1] = 1
        temp += 1
    except:
      None
  except:
    cnt[cur2-nums[i]] = 1
ans = cur2
for i in cnt:
  if cnt[i]:
    ans = min(i,ans)
print pow(x,ans,pow(10,9)+7)
