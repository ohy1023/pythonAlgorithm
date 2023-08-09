import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    dy[0][0] = graph[0][0]
    for i in range(1, n):
        dy[0][i] = dy[0][i - 1] + graph[0][i]
        dy[i][0] = dy[i - 1][0] + graph[i][0]

    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i - 1][j], dy[i][j - 1]) + graph[i][j]

    print(dy[n - 1][n - 1])
