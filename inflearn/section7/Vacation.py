def solution(v, s):
    global res
    if v == n + 1:
        if s > res:
            res = s
    else:
        if v + t[v] <= n + 1:
            solution(v + t[v], s + p[v])
        solution(v + 1, s)


if __name__ == "__main__":
    n = int(input())
    t = [0] * (n + 1)
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        t[i], p[i] = map(int, input().split())

    res = -2147000000
    solution(1, 0)
    print(res)
