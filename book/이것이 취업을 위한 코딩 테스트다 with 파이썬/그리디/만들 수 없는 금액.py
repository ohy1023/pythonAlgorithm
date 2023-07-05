import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    coins = sorted(list(map(int, input().split())))

    target = 1

    for coin in coins:
        if target < coin:
            break
        target += coin
        print(target)

    print(target)
