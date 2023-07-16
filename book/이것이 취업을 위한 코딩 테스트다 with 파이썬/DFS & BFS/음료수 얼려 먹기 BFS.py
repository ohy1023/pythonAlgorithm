import sys
from collections import deque

input = sys.stdin.readline


def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))



if __name__ == "__main__":

    # 입력값 받기
    n, m = map(int, input().split())
    graph = [[int(num) for num in input().strip()] for _ in range(n)]

    # 상하좌우
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 결과값 변수
    cnt = 0

    # 그래프를 순회하면서 얼음 구멍을 찾으면 BFS 실행
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 0:
                cnt += 1
                BFS(a, b)

    print(cnt)
