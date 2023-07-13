import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    withdraw_times = sorted(list(map(int, input().split())))
    res = 0

    for i in range(1, n + 1):
        res += sum(withdraw_times[0:i])

    print(res)
