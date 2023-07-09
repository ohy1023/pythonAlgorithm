import sys

input = sys.stdin.readline

if __name__ == "__main__":
    x, y = 1, 1

    move_type = {}

    move_type["L"] = (0, -1)
    move_type["U"] = (-1, 0)
    move_type["R"] = (0, 1)
    move_type["D"] = (1, 0)

    n = int(input())
    plans = input().split()

    for plan in plans:
        nx = x + move_type[plan][0]
        ny = y + move_type[plan][1]

        if 0 < nx <= n and 0 < ny <= n:
            x, y = nx, ny

    print(x, y)
