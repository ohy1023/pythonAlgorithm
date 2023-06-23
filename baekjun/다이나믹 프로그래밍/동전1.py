import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dy = [0] * (k + 1)
    dy[0] = 1
    for coin in coins:
        for i in range(coin, k + 1):
            if i - coin >= 0:
                dy[i] += dy[i - coin]

    print(dy[k])
