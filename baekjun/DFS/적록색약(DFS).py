import sys

"""
백준 10026 적록색약 (골드 5) - DFS
https://www.acmicpc.net/problem/10026
"""


def DFS(x, y):
    tmp = graph[x][y]

    check[x][y] = True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and not check[nx][ny] and graph[nx][ny] == tmp:
            DFS(nx, ny)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
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
                res1 += 1
                DFS(i, j)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'

    check = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                res2 += 1
                DFS(i, j)

    print(res1, res2, sep=" ")
