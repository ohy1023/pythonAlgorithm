import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    dy = [0] * (n + 1)

    if n == 1:
        print(1)
    elif n == 2:
        print(3)
    else:
        dy[1] = 1
        dy[2] = 3
        for i in range(3, n + 1):
            dy[i] = (dy[i - 1] + 2 * dy[i - 2]) % 796796

        print(dy[n])
