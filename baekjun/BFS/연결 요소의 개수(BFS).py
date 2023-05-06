import sys
from collections import deque

input = sys.stdin.readline


def BFS(v):
    dq = deque()
    dq.append(v)
    checked[v] = 1
    while dq:
        node = dq.popleft()
        for j in graph[node]:
            if checked[j] == 0:
                dq.append(j)
                checked[j] = 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    checked = [0] * (n + 1)
    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        if checked[i] == 0:
            cnt += 1
            BFS(i)

    print(cnt)
