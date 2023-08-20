import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        n = int(input())
        dy = [0] * (n + 1)

        if n <= 2:
            print(n)
        elif n == 3:
            print(4)
        else:
            dy[1] = 1
            dy[2] = 2
            dy[3] = 4
            for i in range(4, n + 1):
                dy[i] = dy[i - 1] + dy[i - 2] + dy[i - 3]

            print(dy[n])
