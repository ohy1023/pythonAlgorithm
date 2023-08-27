import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, x = map(int, input().split())
    visited = list(map(int, input().split()))

    sum_value = 0
    prefix_sum = [0]
    for i in visited:
        sum_value += i
        prefix_sum.append(sum_value)

    res = []
    for j in range(n - x + 1):
        res.append(prefix_sum[j + x] - prefix_sum[j])

    if max(res) == 0:
        print("SAD")
    else:
        print(max(res))
        print(res.count(max(res)))
