import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    warehouses = list(map(int, input().split()))
    dy = [0] * (n + 1)

    dy[0] = warehouses[0]
    dy[1] = max(warehouses[0], warehouses[1])
    for i in range(2, n):
        dy[i] = max(dy[i - 2] + warehouses[i], dy[i - 1])

    print(dy[n - 1])
