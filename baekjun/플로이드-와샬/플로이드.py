import sys

"""
백준 11404 플로이드 (골드 4) - 플로이드-와샬 알고리즘
https://www.acmicpc.net/problem/11404
"""

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    INF = int(1e9)
    dis = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dis[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = min(dis[a][b], c)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dis[i][j] == INF:
                dis[i][j] = 0
        print(*dis[i][1:])
