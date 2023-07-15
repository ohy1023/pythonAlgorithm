import sys

input = sys.stdin.readline


def DFS(x, y):
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 오류 발생 지점 : and 연산 순서 문제
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            DFS(nx, ny)


if __name__ == "__main__":
    # 입력값 받기
    n, m = map(int, input().split())
    graph = [[int(num) for num in input().strip()] for _ in range(n)]

    # 상하좌우
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 결과값 변수
    cnt = 0

    # 그래프를 순회하면서 얼음 구멍을 찾으면 DFS 실행
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 0:
                cnt += 1
                DFS(a, b)

    print(cnt)
