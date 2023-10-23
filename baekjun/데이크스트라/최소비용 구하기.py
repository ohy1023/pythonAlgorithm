import sys
import heapq

"""
백준 1916 최소비용 구하기 (골드 5) - 데이크스트라
https://www.acmicpc.net/problem/1916
"""


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작 노드를 큐에 삽입하고 시작 거리를 0으로 설정
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)  # 큐에서 거리가 가장 짧은 노드 정보를 꺼내옴

        if dist > distance[now]:
            continue  # 현재 거리보다 작은 값이 이미 저장되어 있다면 스킵

        for node, cost in graph[now]:  # 현재 노드와 연결된 노드들을 확인
            new_cost = dist + cost  # 현재 노드를 거쳐서 가는 경우의 새로운 거리
            if new_cost < distance[node]:
                distance[node] = new_cost  # 더 짧은 거리로 갱신
                heapq.heappush(q, (new_cost, node))  # 큐에 새로운 거리와 노드 정보 삽입


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = int(1e9)  # 무한대 값 설정

    N = int(input())  # 도시의 개수 입력
    M = int(input())  # 버스의 개수 입력

    graph = [[] for _ in range(N + 1)]  # 각 도시와 버스의 연결 정보를 저장할 그래프 초기화
    distance = [INF] * (N + 1)  # 시작 노드로부터의 거리를 저장할 리스트 초기화

    for _ in range(M):
        u, v, w = map(int, input().split())  # 버스의 정보 입력
        graph[u].append((v, w))  # u에서 v로 가는 버스가 있으며 비용은 w

    s, e = map(int, input().split())  # 출발 도시와 도착 도시 입력

    dijkstra(s)  # 시작 도시에서 모든 도시까지의 최단 거리 계산

    print(distance[e])  # 출발 도시에서 도착 도시까지의 최단 거리 출력
