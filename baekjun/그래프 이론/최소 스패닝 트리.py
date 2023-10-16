import sys

"""
백준 1197 최소 스패닝 트리 (골드 4) - 그래프 이론
https://www.acmicpc.net/problem/1197
"""


def find_parent(parent, x):
    if x != parent[x]:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    input = sys.stdin.readline

    V, E = map(int, input().split())

    parent = [0] * (V + 1)
    edges = []
    res = 0

    # 초기화: 각 정점을 자기 자신으로 초기화
    for i in range(1, V + 1):
        parent[i] = i

    # 간선 정보 입력
    for _ in range(E):
        a, b, cost, = map(int, input().split())
        edges.append((cost, a, b))

    # 간선을 비용에 따라 오름차순 정렬
    edges.sort()

    # 크루스칼 알고리즘 수행
    for edge in edges:
        cost, a, b = edge

        # 사이클을 형성하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            res += cost

    print(res)