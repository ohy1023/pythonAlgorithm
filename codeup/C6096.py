d = [[0 for _ in range(19)] for _ in range(19)]
for i in range(19):
    d[i] = list(map(int, input().split()))

cnt = int(input())
for _ in range(cnt):
    a, b = map(int, input().split())
    for i in range(19):
        if d[a - 1][i] == 1:
            d[a - 1][i] = 0
        else:
            d[a - 1][i] = 1
        if d[i][b - 1] == 1:
            d[i][b - 1] = 0
        else:
            d[i][b - 1] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=" ")
    print()
