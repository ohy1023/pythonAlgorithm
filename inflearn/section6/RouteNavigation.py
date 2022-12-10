def solution(v):
    global cnt
    if v == n:
        cnt += 1
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                solution(i)
                ch[i] = 0


if __name__ == "__main__":

    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    for _ in range(m):
        s, e = map(int, input().split())
        g[s][e] = 1
    ch[1] = 1
    cnt = 0
    solution(1)
    print(cnt)
