import sys
from collections import deque

"""
백준 7576 토마토 (골드 5) - BFS
https://www.acmicpc.net/problem/7576
"""

if __name__ == "__main__":
    input = sys.stdin.readline
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    res = 0
    dq = deque()
    days = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dq.append((i, j))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 1
                dq.append((nx, ny))
                days[nx][ny] = days[x][y] + 1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                print(-1)
                exit()

            if days[i][j] > res:
                res = days[i][j]

    else:
        print(res)
