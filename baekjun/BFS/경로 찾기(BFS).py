import sys
from collections import deque

"""
백준 11403 경로 찾기 (실버 1) - BFS
https://www.acmicpc.net/problem/11403
"""


def BFS(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for i in range(0, n):
        BFS(i)

    for i in visited:
        print(*i)
