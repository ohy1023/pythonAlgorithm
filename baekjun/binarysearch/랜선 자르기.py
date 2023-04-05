import sys

input = sys.stdin.readline


def count(num):
    cnt = 0
    for line in lines:
        cnt += line // num
    return cnt


if __name__ == "__main__":
    k, n = map(int, input().split())
    lines = [int(input()) for _ in range(k)]
    lt, rt = 1, max(lines)
    res = 0

    while lt <= rt:
        mid = (lt + rt) // 2
        if count(mid) >= n:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)
