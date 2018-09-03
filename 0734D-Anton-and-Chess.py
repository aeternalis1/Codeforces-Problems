N = int(raw_input())
X,Y = map(int,raw_input().split())
arr = [[0,1000000000000] for x in range(8)]

def getdir(a,b,c,d):
    if a==c:
        if b>d:
            return 0
        else:
            return 1
    if b==d:
        if a>c:
            return 2
        else:
            return 3
    if abs(a-c)==abs(b-d):
        if a>c and b>d:
            return 4
        if a>c and b<d:
            return 5
        if a<c and b>d:
            return 6
        if a<c and b<d:
            return 7
    return -1


for i in range(N):
    p,x,y = raw_input().split()
    x = int(x)
    y = int(y)
    cur = getdir(x,y,X,Y)
    if cur==-1:
        continue
    if abs(x-X)+abs(y-Y)<arr[cur][1]:
        arr[cur][1] = abs(x-X)+abs(y-Y)
        if cur<4:
            if p=='B':
                arr[cur][0] = 0
            else:
                arr[cur][0] = 1
        else:
            if p=='R':
                arr[cur][0] = 0
            else:
                arr[cur][0] = 1

ans = 0
for i in range(8):
    if arr[i][0]:
        ans = 1
if ans:
    print "YES"
else:
    print "NO"
