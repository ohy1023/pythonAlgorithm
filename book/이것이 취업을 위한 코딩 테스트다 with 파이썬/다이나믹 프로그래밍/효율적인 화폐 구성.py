import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dy = [10001] * (m + 1)
    dy[0] = 0

    for coin in coins:
        for j in range(1, m + 1):
            if j - coin >= 0:
                dy[j] = min(dy[j - coin] + 1, dy[j])

    if dy[m] == 10001:
        print(-1)
    else:
        print(dy[m])
