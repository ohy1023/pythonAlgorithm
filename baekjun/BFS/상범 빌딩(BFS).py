import sys
from collections import deque

"""
백준 6593 상범 빌딩 (골드 5) - BFS
https://www.acmicpc.net/problem/6593
"""


def BFS(x, y, z):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    dq = deque()

    dq.append((x, y, z))
    visited[x][y][z] = 0

    while dq:
        x, y, z = dq.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c and (
                    graph[nx][ny][nz] == "." or graph[nx][ny][nz] == "E") and visited[nx][ny][
                nz] == 0:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                if graph[nx][ny][nz] == "E":
                    return "Escaped in %d minute(s)." % visited[nx][ny][nz]
                dq.append((nx, ny, nz))

    return "Trapped!"


if __name__ == "__main__":
    input = sys.stdin.readline

    while True:
        l, r, c, = map(int, input().split())

        if l == 0 and r == 0 and c == 0:
            break

        graph = [[] * r for _ in range(l)]
        visited = [[[0] * c for _ in range(r)] for _ in range(l)]

        for i in range(l):
            for _ in range(r):
                graph[i].append(list(map(str, input().strip())))
            input()

        for i in range(l):
            for j in range(r):
                for k in range(c):
                    if graph[i][j][k] == "S":
                        print(BFS(i, j, k))
