import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    temperatures = list(map(int, input().split()))

    end = interval_sum = 0
    res = -2147000000

    for start in range(n - k + 1):
        while end - start < k and end < n:
            interval_sum += temperatures[end]
            end += 1

        if res < interval_sum:
            res = interval_sum

        interval_sum -= temperatures[start]

    print(res)
