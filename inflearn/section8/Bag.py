import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dy = [0] * (m + 1)
for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, m + 1):
        dy[j] = max(dy[j - w] + v, dy[j])

print(dy[m])