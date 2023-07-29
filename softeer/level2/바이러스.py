import sys

input = sys.stdin.readline

k, p, n = map(int, input().split())

for i in range(n):
    k = (k * p) % 1000000007

print(k)


