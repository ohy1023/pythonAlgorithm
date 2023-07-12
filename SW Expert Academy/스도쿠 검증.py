import sys

input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    dx = [0, -1, -1, -1, 0, 0, 1, 1, 1]
    dy = [0, -1, 0, 1, -1, 1, -1, 0, 1]
    points = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
    for i in range(9):
        check_row = [0] * 10
        check_col = [0] * 10
        for j in range(9):
            check_row[board[i][j]] += 1
            check_col[board[j][i]] += 1

        for k in range(1, 10):
            if check_row[k] != 1:
                result = 0
                break
            if check_col[k] != 1:
                result = 0
                break

    for point in points:
        check_grid = [0] * 10

        for j in range(9):
            nx = point[0] + dx[j]
            ny = point[1] + dy[j]

            check_grid[board[nx][ny]] += 1

        for k in range(1, 10):
            if check_grid[k] != 1:
                result = 0
                break

    print("#{} {}".format(tc, result))
