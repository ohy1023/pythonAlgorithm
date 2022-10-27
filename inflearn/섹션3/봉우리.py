n = int(input())
a = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(1, n+1):
    a[i][1:n + 1] = list(map(int, input().split()))

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)
