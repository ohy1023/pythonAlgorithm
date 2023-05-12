import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1:
                dq.append((xx, yy))
                board[xx][yy] = 0


if __name__ == "__main__":

    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        board = [[0] * m for _ in range(n)]
        cnt = 0
        for _ in range(k):
            y, x = map(int, input().split())
            board[x][y] = 1

        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    BFS(i, j)
                    cnt += 1

        print(cnt)
