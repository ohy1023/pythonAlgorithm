def solution(v: int):
    global cnt
    if v == m:
        for j in range(m):
            print(check[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            check[v] = i
            solution(v + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    check = [0] * (m)
    cnt = 0
    solution(0)
    print(cnt)
