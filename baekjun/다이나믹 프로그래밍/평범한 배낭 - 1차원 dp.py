import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(n)]
    dy = [0] * (k + 1)

    for jewel in jewels:
        w, v = jewel[0], jewel[1]
        for j in range(k, 0, -1):
            if w <= j:
                dy[j] = max(dy[j], dy[j - w] + v)

    print(dy[k])
