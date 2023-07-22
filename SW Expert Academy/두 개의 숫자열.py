import sys

input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    res = -21476000000

    if n > m:
        long, short = n, m
        long_arr = list(map(int, input().split()))
        short_arr = list(map(int, input().split()))
    else:
        long, short = m, n
        short_arr = list(map(int, input().split()))
        long_arr = list(map(int, input().split()))

    dif = long - short + 1
    for _ in range(dif):
        tmp = 0
        for a, b in zip(long_arr, short_arr):
            tmp += (a * b)
        if tmp > res:
            res = tmp
        short_arr.insert(0, 0)

    print("#{} {}".format(test_case, res))
