import sys

input = sys.stdin.readline

n = int(input())

bricks = []
for i in range(n):
    a, b, c, = map(int, input().split())
    bricks.append((a, b, c))
bricks.sort(reverse=True)
dy = [0] * n
dy[0] = bricks[0][1]
res = bricks[0][1]
for i in range(1, n):
    max = 0
    for j in range(i - 1, -1, -1):
        if bricks[j][2] > bricks[i][2] and max < dy[j]:
            max = dy[j]
    dy[i] = max + bricks[i][1]

    if res < dy[i]:
        res = dy[i]

print(res)
