import sys
import heapq

"""
백준 1753 최단 경로 (골드 4) - 데이크스트라
https://www.acmicpc.net/problem/1753
"""


def dijkstra(start):
    q = []  # 우선순위 큐
    heapq.heappush(q, (0, start))  # 시작 노드를 큐에 추가
    distance[start] = 0  # 시작 노드까지의 거리를 0으로 초기화

    while q:
        dist, now = heapq.heappop(q)  # 가장 최단 거리를 가진 노드를 꺼냄

        if distance[now] < dist:
            continue  # 이미 처리된 노드라면 무시

        for i in graph[now]:  # 현재 노드와 연결된 다른 노드들을 확인
            cost = dist + i[1]  # 현재 노드를 거쳐 다른 노드로 가는 비용 계산
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # 더 짧은 거리를 발견하면 거리 갱신
                heapq.heappush(q, (cost, i[0]))  # 해당 노드까지의 거리를 큐에 추가


if __name__ == "__main__":
    input = sys.stdin.readline

    INF = int(1e9)  # 무한대 값 설정

    # 노드의 개수, 간선의 개수 입력 받음.
    V, E = map(int, input().split())
    # 시작 지점 입력 받음.
    K = int(input())

    graph = [[] * (V + 1) for _ in range(V + 1)]  # 간선 정보를 저장할 그래프
    distance = [INF] * (V + 1)  # 최단 거리를 저장할 리스트

    # 간선 정보 입력 받음.
    for _ in range(E):
        # u에서 v로 가는 가중치 w인 간선
        u, v, w = map(int, input().split())
        graph[u].append((v, w))  # 간선 정보를 그래프에 추가

    dijkstra(K)  # 데이크스트라 알고리즘 실행

    # 최단 거리 결과 출력 (무한대 값인 경우 "INF" 출력)
    print(*[dist if dist != INF else "INF" for dist in distance[1:]], sep="\n")
