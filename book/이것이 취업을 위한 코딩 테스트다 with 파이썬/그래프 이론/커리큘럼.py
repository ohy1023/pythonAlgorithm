import sys
from collections import deque
import copy

"""
이코테 level.3
커리큘럼 - 위상 정렬
깊은 복사 vs 얇은 복사 (https://blockdmask.tistory.com/576)
"""


# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)  # 수강 시간을 복사 (깊은 복사)
    q = deque()  # 큐

    # 초기 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()  # 큐에서 노드 추출

        # 현재 노드와 연결된 노드들의 진입차수를 감소시키고, 진입차수가 0이 되면 큐에 삽입
        for i in graph[now]:
            # 꺼낸 노드의 최소 수강 시간과 연결된 노드의 기본 수강 시간을 더한 뒤,
            # 해당 값이, 연결된 노드의 최소 수강 시간보다 크다면 해당 값으로 업데이트
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    print(*result[1:], sep="\n")


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    indegree = [0] * (n + 1)  # 진입차수를 나타내는 리스트 초기화
    graph = [[] for i in range(n + 1)]  # 그래프 초기화
    time = [0] * (n + 1)  # 각 과목의 수강 시간을 나타내는 리스트 초기화

    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        time[i] = data[0]  # 과목의 기본 수강 시간 저장
        for x in data[1:-1]:
            indegree[i] += 1  # 진입차수 증가
            graph[x].append(i)  # 간선 정보 추가 (x -> i)

    topology_sort()
