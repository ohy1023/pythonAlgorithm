import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n + 1)
    if n < 3:
        print(n)
    else:
        dy[1] = 1
        dy[2] = 2
        for i in range(3, n + 1):
            dy[i] = dy[i - 2] + dy[i - 1]
        print(dy[n] % 10007)
