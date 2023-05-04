import sys

sys.setrecursionlimit(10 ** 6)

def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and h < board[xx][yy]:
            DFS(xx, yy, h)
    return


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for h in range(max(map(max, board))):
        cnt = 0
        ch = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)

print(res)
