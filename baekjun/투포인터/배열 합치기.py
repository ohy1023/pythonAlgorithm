import sys

"""
백준 11728 배열 합치기 (실버 5) - 투포인터
https://www.acmicpc.net/problem/11728
"""

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    res = []

    i, j = 0, 0
    while i < n or j < m:
        if j >= m or (i < n and list_a[i] <= list_b[j]):
            res.append(list_a[i])
            i += 1
        else:
            res.append(list_b[j])
            j += 1

    print(*res)
