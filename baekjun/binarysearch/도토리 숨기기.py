import sys

input = sys.stdin.readline


def cnt_acorn(value):
    cnt = 0
    for start, end, step, in rules:
        end = min(value, end)
        if start <= end:
            calc_value = (end - start) // step + 1
            cnt += calc_value

    return cnt


if __name__ == "__main__":
    n, k, d = map(int, input().split())
    rules = [list(map(int, input().split())) for _ in range(k)]

    lt, rt = 1, n
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if cnt_acorn(mid) < d:
            lt = mid + 1
        else:
            res = mid
            rt = mid - 1

    print(res)
