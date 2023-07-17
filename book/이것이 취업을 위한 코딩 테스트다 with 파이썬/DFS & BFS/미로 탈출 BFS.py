import sys
from collections import deque

input = sys.stdin.readline


def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(int(num) for num in input().strip()) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    print(BFS(0, 0))
