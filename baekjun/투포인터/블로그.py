import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, x = map(int, input().split())
    visited = list(map(int, input().split()))

    end, interval_sum, max_value, cnt = 0, 0, 0, 1
    for start in range(n - x + 1):
        while end - start < x and end < n:
            interval_sum += visited[end]
            end += 1

        if max_value == interval_sum:
            cnt += 1
        elif max_value < interval_sum:
            max_value = interval_sum
            cnt = 1

        interval_sum -= visited[start]

    if max_value == 0:
        print("SAD")
    else:
        print(max_value)
        print(cnt)
