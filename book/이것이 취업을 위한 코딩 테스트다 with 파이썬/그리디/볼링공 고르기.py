import sys
from itertools import combinations

input = sys.stdin.readline


def sol_simple():
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if balls[i] != balls[j]:
                cnt += 1

    return cnt


def sol_combinations():
    cnt = 0

    com = list(combinations(balls, 2))
    for a, b in com:
        if a != b:
            cnt += 1
    return cnt


def sol_answer():
    global n
    cnt = 0
    arr = [0] * 11

    for ball in balls:
        arr[ball] += 1

    for i in range(1, m + 1):
        n -= arr[i]
        cnt += arr[i] * n

    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    balls = list(map(int, input().split()))

    print(sol_simple())
    print(sol_combinations())
    print(sol_answer())
