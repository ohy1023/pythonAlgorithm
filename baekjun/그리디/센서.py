import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    coordinates = sorted(list(map(int, input().split())))

    dist = []
    for i in range(n - 1):
        dist.append(coordinates[i + 1] - coordinates[i])

    dist.sort()

    print(sum(dist[:n - k]))
