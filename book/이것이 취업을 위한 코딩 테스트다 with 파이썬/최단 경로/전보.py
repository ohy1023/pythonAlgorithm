import sys
import heapq

"""
이코테 level.3
전보 - 데이크스트라 알고리즘 
"""


def dijkstra(start):
    q = []  # 우선순위 큐 초기화
    heapq.heappush(q, (0, start))  # 시작 노드와 시간 0을 넣어줌
    usage_time[start] = 0  # 시작 노드로 가는 시간 0으로 설정

    while q:
        time, now = heapq.heappop(q)  # 가장 가까운 노드와 시간 정보 가져옴

        if usage_time[now] < time:
            continue  # 이미 처리된 노드라면 넘어감

        for node, cost in graph[now]:  # 현재 노드의 인접 노드 순회
            new_time = time + cost  # 현재 노드를 통해 이동할 때의 시간
            if new_time < usage_time[node]:  # 현재 기록된 시간보다 작으면
                usage_time[node] = new_time  # 더 작은 값으로 업데이트하고
                heapq.heappush(q, (new_time, node))  # 큐에 추가하여 다음 노드로 이동


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = int(1e9)

    n, m, c = map(int, input().split())  # 노드 개수, 간선 개수, 시작 노드 입력

    graph = [[] for _ in range(n + 1)]
    usage_time = [INF] * (n + 1)

    for _ in range(m):
        x, y, z = map(int, input().split())  # 간선 정보 입력
        graph[x].append((y, z))

    dijkstra(c)  # 다익스트라 알고리즘 실행

    count = 0  # 도달 가능한 노드 개수 초기화
    max_time = 0  # 최대 시간 초기화
    for d in usage_time:
        if d != INF:  # INF가 아닌 값은 도달 가능한 노드를 의미함
            count += 1  # 도달 가능한 노드 개수 증가
            max_time = max(max_time, d)  # 최대 시간 업데이트

    print(count - 1, max_time)  # 결과 출력
