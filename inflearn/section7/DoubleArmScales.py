def solution(v, s):
    global res
    if v == k:
        if 0 < s <= sum(g):
            res.add(s)
    else:
        solution(v + 1, s + g[v])
        solution(v + 1, s - g[v])
        solution(v + 1, s)


if __name__ == "__main__":
    k = int(input())
    g = list(map(int, input().split()))
    res =set()
    solution(0, 0)
    print(sum(g) - len(res))
