import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, = map(int, input().split())
    dis = [[5000] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        s, e, v = map(int, input().split())
        dis[s][e] = v
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print(0, end=' ')
            elif dis[i][j] == 5000:
                print('M', end=' ')
            else:
                print(dis[i][j], end=' ')
        print()
