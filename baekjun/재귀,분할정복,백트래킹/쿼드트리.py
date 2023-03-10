import sys

input = sys.stdin.readline


def DAC(x, y, size):
    if size == 1:  # 픽셀 하나일 때
        print(board[x][y], end="")
        return
    num = board[x][y]
    for row in range(x, x + size):
        for col in range(y, y + size):
            if num != board[row][col]:
                print("(", end="")
                size //= 2
                DAC(x, y, size)
                DAC(x, y + size, size)
                DAC(x + size, y, size)
                DAC(x + size, y + size, size)
                print(")", end="")
                return
    print(board[x][y], end="")
    return


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(n)]
    DAC(0, 0, n)
