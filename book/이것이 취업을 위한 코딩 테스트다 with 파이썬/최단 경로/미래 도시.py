import sys

"""
이코테 level.2
미래도시 - 플로이드-와샬 알고리즘 
"""

if __name__ == "__main__":
    input = sys.stdin.readline

    INF = int(1e9)

    # 정점의 개수 n, 간선의 개수 m 입력
    n, m = map(int, input().split())

    # 그래프 초기화 (최단 거리를 저장할 테이블)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    # 자기 자신으로 가는 거리는 0으로 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 양방향 간선 정보 입력
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1

    # 최종 목적지 x와 중간 지점 k 입력
    x, k = map(int, input().split())

    # 플로이드-와샬 알고리즘을 통해 최단 거리 계산
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 결과값 계산
    res = graph[1][k] + graph[k][x]

    # 결과값이 무한대(INF)보다 크거나 같으면 -1 출력, 아니면 결과값 출력
    if res >= INF:
        print(-1)
    else:
        print(res)
