n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    r, b, c = map(int, input().split())

    if b == 0:
        for _ in range(c):
            a[r - 1].append(a[r - 1].pop(0))
    else:
        for _ in range(c):
            a[r - 1].insert(0, a[r - 1].pop())

x, y = 0, n-1
ans = 0
for i in range(n):
    for j in range(x,y+1):
        ans +=a[i][j]
    if i < n//2:
        x+=1
        y-=1
    else:
        x-=1
        y+=1

print(ans)
