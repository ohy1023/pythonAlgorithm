def solution(v, s):
    global cnt
    if v == k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        for j in range(s, n):
            res[v] = numbers[j]
            solution(v + 1, j + 1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    res = [0] * k
    solution(0, 0)
    print(cnt)
