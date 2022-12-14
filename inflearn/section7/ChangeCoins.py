def solution(v, s):
    global cnt
    if s > T:
        return
    if v == k:
        if s == T:
            cnt += 1
    else:
        for i in range(N[v] + 1):
            solution(v + 1, s + (P[v] * i))


if __name__ == "__main__":
    T = int(input())
    k = int(input())
    P = list()
    N = list()
    for _ in range(k):
        p, n = map(int, input().split())
        P.append(p)
        N.append(n)
    cnt = 0
    solution(0, 0)
    print(cnt)
