import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    rice_cakes = list(map(int, input().split()))

    lt, rt = 0, max(rice_cakes)
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2

        tmp = sum([x - mid for x in rice_cakes if x > mid])

        if tmp < m:
            rt = mid - 1
        else:
            res = mid
            lt = mid + 1

    print(res)
