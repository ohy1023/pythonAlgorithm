import sys

input = sys.stdin.readline


def DAC(x, y, size):
    global cntMinusOne, cntZero, cntOne

    current = board[x][y]

    for row in range(x, x + size):
        for col in range(y, y + size):
            if current != board[row][col]:
                size //= 3
                DAC(x, y, size)
                DAC(x, y + size, size)
                DAC(x, y + (2 * size), size)
                DAC(x + size, y, size)
                DAC(x + size, y + size, size)
                DAC(x + size, y + (2 * size), size)
                DAC(x + (2 * size), y, size)
                DAC(x + (2 * size), y + size, size)
                DAC(x + (2 * size), y + (2 * size), size)
                return

    if current == -1:
        cntMinusOne += 1
    elif current == 0:
        cntZero += 1
    elif current == 1:
        cntOne += 1


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    cntMinusOne, cntZero, cntOne = 0, 0, 0
    DAC(0, 0, n)
    print(cntMinusOne, cntZero, cntOne, sep='\n')
