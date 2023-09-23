import sys

"""
이코테 level.2
팀 결성 - 서로수 알고리즘 
"""


# 부모 노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


# 두 노드의 부모가 같은지 확인하고 결과를 출력하는 함수
def check_same_parent(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        print("YES")
    else:
        print("NO")


# 두 노드를 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i

    for _ in range(m):
        types, a, b = map(int, input().split())

        if types == 0:
            union_parent(parent, a, b)
        else:
            check_same_parent(parent, a, b)
