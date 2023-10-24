import sys

"""
백준 1389 케빈 베이컨의 6단계 법칙 (실버 1) - 플로이드-와샬 알고리즘
https://www.acmicpc.net/problem/1389
"""

if __name__ == "__main__":
    input = sys.stdin.readline
    INF = int(1e9)
    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신까지의 거리는 0으로 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 친구 관계 입력
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s][e] = graph[e][s] = 1

    # 플로이드-와샬 알고리즘을 통한 최단 경로 계산
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 각 유저마다 케빈 베이컨의 수를 계산하고 최소 값을 출력
    res = [INF]
    for i in range(1, n + 1):
        res.append(sum(graph[i][1:]))

    print(res.index(min(res)))
