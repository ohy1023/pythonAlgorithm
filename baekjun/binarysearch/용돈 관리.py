import sys

input = sys.stdin.readline


def Count(capacity):
    cnt = 1
    sum = 0
    for x in budget:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    budget = [int(input()) for _ in range(n)]
    lt, rt, = 1, sum(budget)
    max_budget = max(budget)
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if mid >= max_budget and Count(mid) <= m:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1
    print(res)
