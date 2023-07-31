import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def DFS(x, y):
    global tmp
    tmp += 1
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            DFS(nx, ny)


if __name__ == "__main__":
    n = int(input())
    board = [list(int(num) for num in input().strip()) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_cnt = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                tmp = 0
                DFS(i, j)
                block_cnt.append(tmp)

    print(len(block_cnt))
    for cnt in sorted(block_cnt):
        print(cnt)
