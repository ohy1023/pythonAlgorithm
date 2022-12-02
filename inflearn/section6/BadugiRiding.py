def DFS(v: int, s: int, t: int):
    global result
    if s + (total - t) < result:
        return
    if s > C:
        return
    if v == N:
        if s > result:
            result = s
    else:
        DFS(v + 1, s + a[v], t + a[v])
        DFS(v + 1, s, t + a[v])


if __name__ == "__main__":
    C, N = map(int, input().split())
    a = [int(input()) for _ in range(N)]
    total = sum(a)
    result = -2147000000
    DFS(0, 0, 0)
    print(result)
