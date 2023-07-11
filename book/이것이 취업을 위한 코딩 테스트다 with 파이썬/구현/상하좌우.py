import sys

input = sys.stdin.readline

if __name__ == "__main__":
    x, y = 1, 1

    hash_map = {"L": (0, -1), "U": (-1, 0), "R": (0, 1), "D": (1, 0)}

    n = int(input())
    plans = input().split()

    for plan in plans:
        nx = x + hash_map[plan][0]
        ny = y + hash_map[plan][1]

        if 0 < nx <= n and 0 < ny <= n:
            x, y = nx, ny

    print(x, y)
