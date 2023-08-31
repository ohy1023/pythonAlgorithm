import sys

"""
백준 10819 차이를 최대로 (실버 2) - 백트래킹
https://www.acmicpc.net/problem/10819
"""


def back_tracking(v):
    global ans
    if v == n:
        tmp = 0
        for i in range(n - 1):
            tmp += abs(res[i] - res[i + 1])

        if tmp > ans:
            ans = tmp

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            res[v] = arr[i]
            back_tracking(v + 1)
            visited[i] = False


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * n
    ans = 0
    res = [0] * n

    back_tracking(0)

    print(ans)
