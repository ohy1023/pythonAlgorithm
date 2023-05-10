import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    wines = [int(input()) for _ in range(n)]
    dy = [0] * n
    if n <= 2:
        print(sum(wines))
    else:
        dy[0] = wines[0]
        dy[1] = wines[0] + wines[1]
        dy[2] = max(wines[1] + wines[2], wines[0] + wines[2], dy[1])
        for i in range(3, n):
            dy[i] = max(dy[i - 2] + wines[i], dy[i - 3] + wines[i - 1] + wines[i], dy[i - 1])
        print(dy[n - 1])
