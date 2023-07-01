import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, l = map(int, input().split())
    points = sorted(list(map(int, input().split())))

    start = points[0] - 0.5
    end = start + l
    count = 1

    for i in range(n):
        if start >= points[i] or points[i] >= end:
            count += 1
            start = points[i] - 0.5
            end = start + l

    print(count)