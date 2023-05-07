import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def DFS(v):
    checked[v] = 1
    for j in graph[v]:
        if checked[j] == 0:
            DFS(j)


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    checked = [0] * (n + 1)
    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        if checked[i] == 0:
            cnt += 1
            DFS(i)

    print(cnt)
