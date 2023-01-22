from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_num = -2147000000
min_num = 2147000000

for row in board:
    min_tmp = min(row)
    max_tmp = max(row)
    if min_tmp < min_num:
        min_num = min_tmp
    if max_tmp > max_num:
        max_num = max_tmp

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
Q = deque()

for rain in range(min_num, max_num):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and rain < board[i][j]:
                ch[i][j] = 1
                Q.append((i, j))
                while Q:
                    tmp = Q.popleft()
                    for k in range(4):
                        x = tmp[0] + dx[k]
                        y = tmp[1] + dy[k]
                        if 0 <= x < n and 0 <= y < n and ch[x][y] == 0 and rain < board[x][y]:
                            ch[x][y] = 1
                            Q.append((x, y))
                cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)
