from collections import deque


def BFS(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1:
                if visited[xx][yy] == 0 or visited[xx][yy] > visited[x][y] + 1:
                    queue.append((xx, yy))
                    visited[xx][yy] = visited[x][y] + 1

    return visited[n - 1][m - 1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    print(BFS(0, 0))
