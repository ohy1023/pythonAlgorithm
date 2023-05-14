import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def BFS():
    global res
    dq = deque()
    for wall_combi in combinations(empty, 3):
        temp = copy.deepcopy(board)
        for x_w, y_w in wall_combi:
            temp[x_w][y_w] = 1

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

        cnt = 0
        for i in range(n):
            cnt += temp[i].count(0)
        res = max(cnt, res)



if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    empty = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 0]
    res = 0
    BFS()
    print(res)
