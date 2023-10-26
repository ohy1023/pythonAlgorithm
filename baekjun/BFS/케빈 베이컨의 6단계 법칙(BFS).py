import sys
from collections import deque

"""
백준 1389 케빈 베이컨의 6단계 법칙 (실버 1) - BFS
https://www.acmicpc.net/problem/1389
"""


def BFS(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        target = q.popleft()
        for i in graph[target]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[target] + 1
                q.append(i)


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = int(1e9)
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    res = [INF]

    for i in range(1, n + 1):
        distance = [0 for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        BFS(i)
        res.append(sum(distance))

    print(res.index(min(res)))
