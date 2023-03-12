import sys

input = sys.stdin.readline


def DAC(N, r, c):
    if N == 0:
        return 0

    return 2 * (r % 2) + (c % 2) + 4 * DAC(N - 1, r // 2, c // 2)


if __name__ == "__main__":
    n, r, c = map(int, input().split())
    print(DAC(n, r, c))
