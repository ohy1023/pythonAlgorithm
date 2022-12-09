import sys

n, m = map(int, input().split())
G = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().strip().split())
    G[s][e] = w

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(G[i][j], end=" ")
    print()