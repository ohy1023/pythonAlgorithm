import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dy = [[0] * n for _ in range(n)]

dy[0][0] = board[0][0]
for i in range(1, n):
    dy[0][i] = dy[0][i - 1] + board[0][i]
    dy[i][0] = dy[i - 1][0] + board[i][0]
    for j in range(1, n):
        for k in range(1, n):
            dy[j][k] = min(dy[j - 1][k], dy[j][k - 1]) + board[j][k]

print(dy[n - 1][n - 1])
