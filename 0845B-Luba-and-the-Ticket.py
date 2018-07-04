num = list(raw_input())
arr1 = [int(x) for x in num[:3]]
arr2 = [int(x) for x in num[3:]]
ans1 = [10 for x in range(28)]
ans2 = [10 for x in range(28)]
for i in range(10):
  for j in range(10):
    for k in range(10):
      cur = 3
      if i==arr1[0]:
        cur -= 1
      if j==arr1[1]:
        cur -= 1
      if k==arr1[2]:
        cur -= 1
      ans1[i+j+k] = min(ans1[i+j+k],cur)
for i in range(10):
  for j in range(10):
    for k in range(10):
      cur = 3
      if i==arr2[0]:
        cur -= 1
      if j==arr2[1]:
        cur -= 1
      if k==arr2[2]:
        cur -= 1
      ans2[i+j+k] = min(ans2[i+j+k],cur)
ans = 10
for i in range(28):
  ans = min(ans,ans1[i]+ans2[i])
print ans
