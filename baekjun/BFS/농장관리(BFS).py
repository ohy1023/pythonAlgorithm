import sys
from collections import deque

"""
백준 1245 농장 관리 (골드 5) - BFS
https://www.acmicpc.net/problem/1245
"""


def BFS(x, y):
    global flag

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    dq = deque()
    dq.append((x, y))

    baseline = graph[x][y]

    visited[x][y] = True

    while dq:
        x, y = dq.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > baseline:
                    flag = False
                if not visited[nx][ny] and graph[nx][ny] == baseline:
                    visited[nx][ny] = True
                    dq.append((nx, ny))


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    res = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                flag = True
                BFS(i, j)
                if flag:
                    res += 1
    print(res)
