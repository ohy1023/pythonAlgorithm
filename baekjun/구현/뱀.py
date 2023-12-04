import sys
from collections import deque

"""
백준 3190 뱀 (골드 4) - 구현
https://www.acmicpc.net/problem/3190
"""


def turn(next_direct):
    global d
    if next_direct == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4

    return d


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    K = int(input())

    graph = [[0] * (N + 1) for _ in range(N + 1)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 2

    info = dict()

    L = int(input())

    for _ in range(L):
        s, d = input().split()
        info[int(s)] = d

    x, y = 1, 1
    graph[x][y] = 1
    time = 0
    d = 0
    snakes = deque([(x, y)])

    while True:
        nx, ny = x + dx[d], y + dy[d]

        if 1 <= nx <= N and 1 <= ny <= N and graph[nx][ny] != 1:
            # 사과가 아니면 꼬리 제거
            if graph[nx][ny] != 2:
                a, b = snakes.popleft()
                graph[a][b] = 0

            x, y = nx, ny
            graph[x][y] = 1
            snakes.append((x, y))

            time += 1

            if time in info.keys():
                turn(info[time])

        else:
            time += 1
            break

    print(time)
