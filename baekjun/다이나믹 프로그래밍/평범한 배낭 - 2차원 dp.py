import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(n)]
    jewels.insert(0, (0, 0))
    dy = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = jewels[i][0], jewels[i][1]
        for j in range(1, k + 1):
            if w <= j:
                dy[i][j] = max(dy[i - 1][j], dy[i - 1][j - w] + v)
            else:
                dy[i][j] = dy[i - 1][j]

    print(dy[n][k])
