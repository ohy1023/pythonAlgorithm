import sys

"""
백준 2003 수들의 합2 (실버 4) - 투포인터
https://www.acmicpc.net/problem/2003
"""

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    cnt, end, interval_sum = 0, 0, 0

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += nums[end]
            end += 1

        if interval_sum == m:
            cnt += 1
        interval_sum -= nums[start]

    print(cnt)
