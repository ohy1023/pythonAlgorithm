import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    rgb_dist = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):
        rgb_dist[i][0] += min(rgb_dist[i - 1][1], rgb_dist[i - 1][2])

        rgb_dist[i][1] += min(rgb_dist[i - 1][0], rgb_dist[i - 1][2])

        rgb_dist[i][2] += min(rgb_dist[i - 1][0], rgb_dist[i - 1][1])

    print(min(rgb_dist[n - 1]))
