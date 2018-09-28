n,m = map(int,raw_input().split())
nums = list(map(int,raw_input().split()))
cnt = [0 for x in range(m+1)]
ans = n/m
for i in nums:
    if i<=m:
        cnt[i] += 1
ans2 = 0
for i in range(n):
    if nums[i]>m or (nums[i]<=m and cnt[nums[i]]>ans):
        for j in range(1,m+1):
            if cnt[j]<ans:
                if nums[i]<=m:
                    cnt[nums[i]] -= 1
                cnt[j] += 1
                nums[i] = j
                ans2 += 1
                break
print ans,ans2
print " ".join([str(x) for x in nums])
