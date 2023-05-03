import sys

sys.setrecursionlimit(10 ** 6)

def DFS(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    if x == (n - 1) and y == (m - 1):
        return

    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1:
                if visited[xx][yy] == 0 or visited[xx][yy] > visited[x][y] + 1:
                    visited[xx][yy] = visited[x][y] + 1
                    DFS(xx, yy)

        return visited[n - 1][m - 1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    print(DFS(0, 0))
