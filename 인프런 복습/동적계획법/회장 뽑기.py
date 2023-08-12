import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    INF = int(1e9)
    n = int(input())
    friendship = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        friendship[i][i] = 0

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break

        friendship[a][b] = 1
        friendship[b][a] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                friendship[i][j] = min(friendship[i][j], friendship[i][k] + friendship[k][j])

    res = [0] * n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res[i - 1] = max(res[i - 1], friendship[i][j])

    print(min(res), res.count(min(res)), sep=' ')
    for idx, score in enumerate(res):
        if score == min(res):
            print(idx + 1, end=' ')
