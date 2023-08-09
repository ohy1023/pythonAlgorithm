import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dy = [10001] * (m + 1)
    dy[0] = 0
    for i in range(n):
        for j in range(coins[i], m + 1):
            if j - coins[i] >= 0:
                dy[j] = min(dy[j], dy[j - coins[i]] + 1)

    print(dy[m])
