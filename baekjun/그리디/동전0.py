import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    cnt = 0
    coins = sorted([int(input()) for _ in range(n)], reverse=True)
    for coin in coins:
        cnt += k // coin
        k %= coin

    print(cnt)
