def dfs(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[x][y] < board[xx][yy]:
                ch[xx][yy] = 1
                dfs(xx, yy)
                ch[xx][yy] = 0


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    maxNum = -2147000000
    minNum = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] < minNum:
                minNum = board[i][j]
                sx = i
                sy = j
            if board[i][j] > maxNum:
                maxNum = board[i][j]
                ex = i
                ey = j
    ch[sx][sy] = 1
    dfs(sx, sy)
    print(cnt)
