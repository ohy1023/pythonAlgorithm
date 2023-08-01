import sys

input = sys.stdin.readline

n = int(input())
dy = [0] * 16

dy[0] = 2

for i in range(1, n + 1):
    dy[i] = dy[i - 1] + 2 ** (i - 1)

print(dy[n]**2)
