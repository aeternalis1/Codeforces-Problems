n = int(raw_input())
nums = list(map(int,raw_input().split()))
cnt = [0 for x in range(101)]
for i in nums:
    cnt[i] += 1
ext = 0
for i in range(101):
    if cnt[i]>2:
        ext += 1
ans = ["" for x in range(n)]
cnt1 = 0
cnt2 = 0
for i in range(n):
    if cnt[nums[i]]==1:
        if cnt1>cnt2:
            ans[i] = 'B'
            cnt2 += 1
        else:
            ans[i] = 'A'
            cnt1 += 1
if cnt1 != cnt2 and not ext:
    print "NO"
else:
    print "YES"
    if cnt1==cnt2:
        for i in range(n):
            if cnt[nums[i]]!=1:
                ans[i] = 'A'
        print "".join(ans)
    else:
        for i in range(101):
            if cnt[i]>2:
                for j in range(n):
                    if nums[j]==i:
                        ans[j] = 'B'
                        break
                break
        for i in range(n):
            if ans[i]=="":
                ans[i] = 'A'
        print "".join(ans)
