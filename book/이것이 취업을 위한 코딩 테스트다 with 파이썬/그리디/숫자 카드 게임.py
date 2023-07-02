import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for i in range(n):
        if res < min(board[i]):
            res = min(board[i])

    print(res)