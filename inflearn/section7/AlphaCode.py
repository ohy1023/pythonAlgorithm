def solution(v, p):
    global cnt
    if v == n:
        cnt += 1
        for j in range(p):
            print(chr(64 + res[j]), end='')
        print()
    else:
        for i in range(1, 27):
            if code[v] == i:
                res[p] = i
                solution(v + 1, p + 1)
            elif i >= 10 and code[v] == i // 10 and code[v] == i % 10:
                res[p] = i
                solution(v + 2, p + 1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0] * (n + 3)
    cnt = 0
    solution(0, 0)
    print(cnt)
