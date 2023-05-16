import sys

input = sys.stdin.readline


def get_count(t):
    cnt = 0
    for i in minutes:
        cnt += t // i
    return cnt


def adjust(a, n):
    th = []
    for idx, i in enumerate(minutes):
        if a % i == 0:
            th.append(idx)
    return th[n - 1] + 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    minutes = list(map(int, input().split()))
    if n <= m:
        print(n)
    else:
        res = 0
        lt, rt = min(minutes), max(minutes) * n
        while lt <= rt:
            mid = (lt + rt) // 2
            if get_count(mid) >= n - m:
                rt = mid - 1
                res = mid
            else:
                lt = mid + 1

        k = n - m - get_count(res - 1)
        print(adjust(res, k))
