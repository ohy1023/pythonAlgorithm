import sys


def solution(v):
    global answer
    if v == n:
        answer = 0
        for i in range(len(mul)):
            answer += res[i] * mul[i]
        if answer == m:
            for k in res:
                print(k, end=' ')
            sys.exit(0)
    else:
        for j in range(1, n + 1):
            if ch[j] == 0:
                ch[j] = 1
                res[v] = j
                solution(v + 1)
                ch[j] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    mul = [1] * n
    ch = [0] * (n + 1)
    answer = 0
    for i in range(1, n):
        mul[i] = mul[i - 1] * (n - i) // i
    solution(0)
