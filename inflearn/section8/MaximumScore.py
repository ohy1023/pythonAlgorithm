import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dy = [0] * (m + 1)
for i in range(n):
    s, t = map(int, input().split())
    for j in range(m, t - 1, -1):
        dy[j] = max(dy[j - t] + s, dy[j])

print(dy[m])
