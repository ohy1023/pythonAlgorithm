def solution(v, s, t):
    global maxTemp
    if t > m:
        return
    if v == n:
        if s > maxTemp:
            maxTemp = s
    else:
        solution(v + 1, s + scores[v], t + times[v])
        solution(v + 1, s, t)


if __name__ == "__main__":
    n, m = map(int, input().split())
    times = [0] * n
    scores = [0] * n
    for i in range(n):
        scores[i], times[i] = map(int, input().split())
    maxTemp = -2147000000
    solution(0, 0, 0)
    print(maxTemp)
