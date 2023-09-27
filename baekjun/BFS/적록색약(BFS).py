import sys
from collections import deque

"""
백준 10026 적록색약 (골드 5) - BFS
https://www.acmicpc.net/problem/10026
"""


def BFS(x, y):
    dq = deque()
    dq.append((x, y))

    tmp = graph[x][y]

    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not check[nx][ny] and graph[nx][ny] == tmp:
                check[nx][ny] = True
                dq.append((nx, ny))


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())

    graph = [[x for x in input().strip()] for _ in range(n)]
    check = [[False] * n for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    res1 = 0
    res2 = 0

    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                check[i][j] = True
                res1 += 1
                BFS(i, j)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'

    check = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                check[i][j] = True
                res2 += 1
                BFS(i, j)

    print(res1, res2, sep=" ")
