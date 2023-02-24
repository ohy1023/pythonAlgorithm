import sys

input = sys.stdin.readline

n = int(input())
coins = list(map(int, input().split()))
m = int(input())
dy = [500] * (m + 1)
dy[0] = 0
for i in coins:
    for j in range(i, m + 1):
        dy[j] = min(dy[j - i] + 1, dy[j])

print(dy[m])
