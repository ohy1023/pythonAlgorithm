import sys

"""
백준 1388 바닥 장식 (실버 4) - DFS
https://www.acmicpc.net/problem/1388
"""


input = sys.stdin.readline


def DFS(x, y):
    d = [-1, 1]
    if graph[x][y] == '-':

        graph[x][y] = ''

        for i in range(2):
            ny = y + d[i]

            if 0 <= ny < m and graph[x][ny] == '-':
                DFS(x, ny)
    elif graph[x][y] == '|':
        graph[x][y] = ''

        for i in range(2):
            nx = x + d[i]

            if 0 <= nx < n and graph[nx][y] == '|':
                DFS(nx, y)


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(input().strip()) for _ in range(n)]

    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '-' or graph[i][j] == '|':
                res += 1
                DFS(i, j)

    print(res)
