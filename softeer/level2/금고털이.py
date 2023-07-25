import sys

input = sys.stdin.readline

w, n = map(int, input().split())

jewels = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: -x[1])

res = 0
for jewel in jewels:
    m, p = jewel[0], jewel[1]
    if w >= m:
        res += (m * p)
        w -= m
    else:
        res += (w * p)
        break
print(res)