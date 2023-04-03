import sys

input = sys.stdin.readline


def Count(capacity):
    cnt = 1
    sum = 0
    for x in lecture:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    lecture = list(map(int, input().split()))
    lt, rt = 1, sum(lecture)
    maxx = max(lecture)
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if mid >= maxx and Count(mid) <= m:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1
    print(res)
