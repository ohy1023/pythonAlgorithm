import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    coins = [500, 100, 50, 10]
    res = 0
    for coin in coins:
        res += n // coin
        n %= coin

    print(res)
