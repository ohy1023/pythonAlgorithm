import sys

input = sys.stdin.readline

n = int(input())
graph = [[100] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

while True:
    s, e = map(int, input().split())
    if s == -1 and e == -1:
        break
    graph[s][e], graph[e][s] = 1, 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

res = [0] * (n + 1)
score = 100
for i in range(1, n + 1):
    for j in range(1, n + 1):
        res[i] = max(res[i], graph[i][j])
    score = min(score, res[i])

out = []
for i in range(1, n + 1):
    if res[i] == score:
        out.append(i)

print("%d %d" %(score, len(out)))
for x in out:
    print(x, end=' ')

