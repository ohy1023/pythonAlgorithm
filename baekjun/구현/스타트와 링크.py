import sys


def backTracking(depth, idx):
    global min_value
    if depth == n // 2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    power1 += graph[i][j]
                elif not visit[i] and not visit[j]:
                    power2 += graph[i][j]
        min_value = min(min_value, abs(power1 - power2))
        return

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            backTracking(depth + 1, i + 1)
            visit[i] = False


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visit = [False for _ in range(n)]
    min_value = 2147000000

    backTracking(0, 0)
    print(min_value)
