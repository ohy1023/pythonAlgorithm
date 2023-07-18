import sys

input = sys.stdin.readline


def DFS(x, y):
    global res, cnt
    # 목적지 도착
    if x == (n - 1) and y == (m - 1):
        if res > cnt:
            res = cnt
        return

    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            cnt += 1
            DFS(nx, ny)
            cnt -= 1
            visited[nx][ny] = False


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(int(num) for num in input().strip()) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited = [[False] * m for _ in range(n)]

    res = 2_147_000_000
    cnt = 1

    visited[0][0] = True
    DFS(0, 0)

    print(res)
