import sys
import copy

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def virus(x, y, arr):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 0:
            arr[xx][yy] = 2
            virus(xx, yy, arr)


def DFS(v):
    global res
    if v == 3:
        temp = copy.deepcopy(board)
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j, temp)
        cnt = 0
        for i in range(n):
            cnt += temp[i].count(0)
        res = max(cnt, res)
        return
    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    board[i][j] = 1
                    DFS(v + 1)
                    board[i][j] = 0


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    DFS(0)
    print(res)
