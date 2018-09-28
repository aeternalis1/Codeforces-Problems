n,m,k = map(int,raw_input().split())
grid = [['.' for x in range(m+2)]]
for i in range(n):
    grid.append(['.']+list(raw_input())+['.'])
grid.append(['.' for x in range(m+2)])
chk = [[0 for x in range(m+2)] for x in range(n+2)]
cur = 1
moves = [[0,1],[0,-1],[1,0],[-1,0]]
lakes = []
for i in range(n+2):
    for j in range(m+2):
        if not chk[i][j] and grid[i][j]=='.':
            queue = [[i,j]]
            chk[i][j] = cur
            res = 1
            while queue:
                c = queue.pop(0)
                for l in moves:
                    y,x = c[0]+l[0],c[1]+l[1]
                    if y>=n+2 or y < 0 or x >= m+2 or x < 0:
                        continue
                    if grid[y][x]=='.' and not chk[y][x]:
                        queue.append([y,x])
                        chk[y][x] = cur
                        res += 1
            if i!=0:
                lakes.append([res,i,j])
lakes = sorted(lakes)
ans = 0
for i in range(len(lakes)-k):
    queue = [[lakes[i][1],lakes[i][2]]]
    grid[lakes[i][1]][lakes[i][2]] = '*'
    while queue:
        c = queue.pop(0)
        for l in moves:
            y,x = c[0]+l[0],c[1]+l[1]
            if y>=n+2 or y < 0 or x >= m+2 or x < 0:
                continue
            if grid[y][x]=='.':
                queue.append([y,x])
                grid[y][x] = '*'
    ans += lakes[i][0]
print ans
for i in range(1,n+1):
    print "".join(grid[i][1:-1])
