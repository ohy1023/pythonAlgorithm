import sys
from collections import deque


# 위상 정렬 함수
def topology_sort():
    result = []  # 위상 정렬 결과를 담을 리스트
    q = deque()  # 큐

    # 초기 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1, v + 1):
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

    # 위상 정렬 결과 출력
    """
    *은 파이썬에서 사용되는 특별한 연산자로, "언패킹"이라고도 불립니다. 
    print(*result)에서 *result를 사용하는 것은 리스트나 튜플 등의 iterable(순회 가능한) 객체를 언패킹하여
    그 안의 요소들을 개별적으로 출력하라는 의미입니다.
    """
    print(*result)


if __name__ == "__main__":
    input = sys.stdin.readline

    v, e = map(int, input().split())  # 노드 개수(v)와 간선 개수(e) 입력
    indegree = [0] * (v + 1)  # 진입차수를 나타내는 리스트 초기화

    graph = [[] for i in range(v + 1)]  # 그래프 초기화

    # 간선 정보 입력 및 진입차수 계산
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)  # 노드 a에서 노드 b로 향하는 간선 정보 저장
        indegree[b] += 1  # 노드 b의 진입차수 증가

    topology_sort()  # 위상 정렬 수행
