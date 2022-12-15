def solution(v):
    global minNum
    if v == n:
        tmp = set(res)
        if len(tmp) == 3 and max(res) - min(res) < minNum:
            minNum = max(res) - min(res)
    else:
        for i in range(3):
            res[i] += coins[v]
            solution(v + 1)
            res[i] -= coins[v]


if __name__ == "__main__":
    n = int(input())
    coins = [int(input()) for _ in range(n)]
    res = [0] * 3
    minNum = 2147000000
    solution(0)
    print(minNum)
