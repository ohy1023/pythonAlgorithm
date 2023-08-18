import sys


def back_tracking(depth):
    if depth == m:
        get_min_dist()
        return

    for e, (cx, cy) in enumerate(chickens):
        if not visited[cx][cy]:
            if t:
                if e < t[-1][0]:
                    continue
            visited[cx][cy] = True
            t.append((e, (cx, cy)))
            back_tracking(depth + 1)
            visited[cx][cy] = False
            t.pop()


def get_min_dist():
    min_dist = 0
    for hx, hy in houses:
        tmp = 2147000000
        for e, (cx, cy) in t:
            value = abs(hx - cx) + abs(hy - cy)

            if tmp > value:
                tmp = value
        min_dist += tmp
    res.append(min_dist)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    t = []
    houses = []
    chickens = []
    visited = [[False] * n for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                houses.append((i, j))
            elif graph[i][j] == 2:
                chickens.append((i, j))

    back_tracking(0)
    print(min(res))
