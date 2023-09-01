import sys
from collections import deque

"""
백준 1260 DFS와 BFS (실버 2) - DFS/BFS
https://www.acmicpc.net/problem/1260
"""


def DFS(depth):
    visited_dfs[depth] = True
    print(depth, end=" ")
    for i in range(1, n + 1):
        if graph[depth][i] == 1 and not visited_dfs[i]:
            visited_dfs[i] = True
            DFS(i)


def BFS(depth):
    dq = deque()
    dq.append(depth)

    visited_bfs[depth] = True

    while dq:
        node = dq.popleft()
        print(node, end=" ")

        for i in range(1, n + 1):
            if graph[node][i] == 1 and not visited_bfs[i]:
                visited_bfs[i] = True
                dq.append(i)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, v = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited_dfs = [False] * (n + 1)
    visited_bfs = [False] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1

    DFS(v)
    print()
    BFS(v)
