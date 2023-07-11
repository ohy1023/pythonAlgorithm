import sys

input = sys.stdin.readline


def change_direction():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    board[x][y] = 1
    res = 1
    times = 0
    while True:
        change_direction()
        nx = x + dx[d]
        ny = y + dy[d]

        if board[nx][ny] == 0:
            x, y = nx, ny
            res += 1
            board[x][y] = 1
            times = 0
            continue
        else:
            times += 1

        if times == 4:
            nx = x - dx[d]
            ny = y - dy[d]

            if board[nx][ny] == 0:
                x, y = nx, ny
            else:
                break
            times = 0

    print(res)
