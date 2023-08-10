import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    problems = [tuple(map(int, input().split())) for _ in range(n)]
    problems.insert(0, (0, 0))

    dy = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        score, time = problems[i][0], problems[i][1]
        for j in range(1, m + 1):
            if time <= j:
                dy[i][j] = max(dy[i - 1][j], dy[i - 1][j - time] + score)
            else:
                dy[i][j] = dy[i - 1][j]

    print(dy[n][m])
