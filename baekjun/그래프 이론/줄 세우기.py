import sys
from collections import deque

"""
백준 2252 줄 세우기 (골드 3) - 위상 정렬
https://www.acmicpc.net/problem/2252
"""


# 위상 정렬 함수
def topology_sort():
    result = []  # 위상 정렬 결과를 담을 리스트
    q = deque()  # 큐

    # 초기 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()  # 큐에서 노드 추출
        result.append(now)  # 추출한 노드를 결과 리스트에 추가

        # 현재 노드와 연결된 노드들의 진입차수를 감소시키고, 진입차수가 0이 되면 큐에 삽입
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(*result)


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    indegree = [0] * (n + 1)

    graph = [[] for i in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)  # 노드 a에서 노드 b로 향하는 간선 정보 저장
        indegree[b] += 1  # 노드 b의 진입차수 증가

    topology_sort()
