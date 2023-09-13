import sys
from collections import deque

"""
백준 1743 음식물 피하기 (실버 1) - BFS
https://www.acmicpc.net/problem/1743
"""


def BFS(x, y):
    cnt = 1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    graph[x][y] = 0

    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1 <= nx <= n and 1 <= ny <= m and graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                dq.append((nx, ny))

    return cnt


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] == 1:
                count = BFS(i, j)
                if res < count:
                    res = count

    print(res)
