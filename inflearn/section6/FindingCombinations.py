def solution(v, s):
    global cnt
    if v == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for j in range(s, n + 1):
            res[v] = j
            solution(v + 1, j + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    solution(0, 1)
    print(cnt)
