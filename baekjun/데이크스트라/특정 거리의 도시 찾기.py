import sys
import heapq

"""
백준 18352 특정 거리의 도시 찾기 (실버 2) - 데이크스트라
https://www.acmicpc.net/problem/18352
"""


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = int(1e9)
    n, m, k, x = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    distance = [INF] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append((b, 1))

    dijkstra(x)

    indices = [index for index, value in enumerate(distance) if value == k]

    if len(indices) == 0:
        print(-1)
    else:
        for index in indices:
            print(index)
