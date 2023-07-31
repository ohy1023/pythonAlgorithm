import sys
from collections import deque

input = sys.stdin.readline


def BFS(x, y):
    dq = deque()
    dq.append((x, y))

    board[x][y] = 0
    count = 1

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                board[nx][ny] = 0
                count += 1
                dq.append((nx, ny))

    block_cnt.append(count)


if __name__ == "__main__":
    n = int(input())
    board = [list(int(num) for num in input().strip()) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_cnt = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                BFS(i, j)

    print(len(block_cnt))
    for cnt in sorted(block_cnt):
        print(cnt)
