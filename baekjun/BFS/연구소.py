import sys
from collections import deque
import copy

input = sys.stdin.readline


def BFS():
    global res
    dq = deque()
    temp = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < m and temp[xx][yy] == 0:
                temp[xx][yy] = 2
                dq.append((xx, yy))

    res = max(get_count(temp), res)


def get_count(arr):
    cnt = 0
    for i in range(n):
        cnt += arr[i].count(0)
    return cnt


def make_wall(cnt):
    if cnt == 3:
        BFS()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(cnt + 1)
                board[i][j] = 0


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    make_wall(0)
    print(res)
