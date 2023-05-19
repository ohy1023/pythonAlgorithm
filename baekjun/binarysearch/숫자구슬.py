import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    marbles = list(map(int, input().split()))

    res = 0
    groups = []
    lt, rt = max(marbles), sum(marbles)
    while lt <= rt:
        mid = (lt + rt) // 2

        group_cnt = 0
        idx = 0
        groups = []

        while idx < n:
            sub_sum = 0
            sub_cnt = 0
            while idx < n and sub_sum + marbles[idx] <= mid:
                sub_sum += marbles[idx]
                sub_cnt += 1
                idx += 1
                if m - group_cnt == n - (idx - 1):
                    break

            group_cnt += 1
            groups.append(sub_cnt)

        if group_cnt <= m:
            rt -= 1
            res = mid
        else:
            lt += 1

    print(res)
    print(*groups)
