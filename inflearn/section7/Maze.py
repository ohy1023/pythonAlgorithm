def dfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and a[xx][yy] == 0:
                a[xx][yy] = 1
                dfs(xx, yy)
                a[xx][yy] = 0


if __name__ == "__main__":
    cnt = 0
    a = [list(map(int, input().split())) for _ in range(7)]
    a[0][0] = 1
    dfs(0, 0)
    print(cnt)
