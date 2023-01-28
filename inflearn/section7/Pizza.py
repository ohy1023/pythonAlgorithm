def DFS(x, y):
    global res
    if x == m:
        sum = 0
        for j in range(len(ha)):
            x1 = ha[j][0]
            y1 = ha[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pa[x][0]
                y2 = pa[x][1]
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        for i in range(y, len(pa)):
            cb[x] = i
            DFS(x + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    pa = []
    ha = []
    cb = [0] * m
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                ha.append((i, j))
            elif board[i][j] == 2:
                pa.append((i, j))
    DFS(0, 0)
    print(res)
