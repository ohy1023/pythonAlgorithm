h, w = map(int, input().split())

m = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            m[x][y + j] = 1
    else:
        for j in range(l):
            m[x + j][y] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(m[i][j], end=' ')
    print()
